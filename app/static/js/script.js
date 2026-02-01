/**
 * Sentiment Analysis Application - Frontend Script
 * ================================================
 * Handles UI interactions, API calls, and result visualization
 */

// Global variables
let currentChart = null;
const MAX_CHARACTERS = 5000;

// ==================== DOM Element Initialization ====================

document.addEventListener("DOMContentLoaded", function () {
  initializeEventListeners();
  setupTabNavigation();
  setupTextInput();
  setupFileUpload();
  setupBatchAnalysis();
});

function initializeEventListeners() {
  // Analyze button
  document.getElementById("analyzeBtn").addEventListener("click", analyzeText);
  document
    .getElementById("textInput")
    .addEventListener("keydown", function (e) {
      if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
        analyzeText();
      }
    });

  // Character counter
  document
    .getElementById("textInput")
    .addEventListener("input", updateCharCount);

  // Batch analysis
  document
    .getElementById("batchAnalyzeBtn")
    .addEventListener("click", batchAnalyze);
}

// ==================== Tab Navigation ====================

function setupTabNavigation() {
  const tabButtons = document.querySelectorAll(".tab-btn");
  const tabContents = document.querySelectorAll(".tab-content");

  tabButtons.forEach((button) => {
    button.addEventListener("click", function () {
      const tabName = this.getAttribute("data-tab");

      // Remove active class from all tabs
      tabButtons.forEach((btn) => btn.classList.remove("active"));
      tabContents.forEach((content) => content.classList.remove("active"));

      // Add active class to clicked tab
      this.classList.add("active");
      document.getElementById(tabName).classList.add("active");

      // Hide results section when switching tabs
      document.getElementById("resultsSection").style.display = "none";
    });
  });
}

// ==================== Text Input Handling ====================

function setupTextInput() {
  const textInput = document.getElementById("textInput");
  updateCharCount();
}

function updateCharCount() {
  const textInput = document.getElementById("textInput");
  const charCount = textInput.value.length;
  const charCountDisplay = document.getElementById("charCount");

  charCountDisplay.textContent = `${charCount} / ${MAX_CHARACTERS}`;

  // Change color if limit is approaching
  if (charCount > MAX_CHARACTERS * 0.9) {
    charCountDisplay.style.color = "#ef4444";
  } else if (charCount > MAX_CHARACTERS * 0.7) {
    charCountDisplay.style.color = "#f59e0b";
  } else {
    charCountDisplay.style.color = "#64748b";
  }
}

async function analyzeText() {
  const text = document.getElementById("textInput").value.trim();

  if (!text) {
    showError("Please enter some text to analyze");
    return;
  }

  if (text.length > MAX_CHARACTERS) {
    showError(`Text exceeds maximum length of ${MAX_CHARACTERS} characters`);
    return;
  }

  await performAnalysis({ text }, "single");
}

// ==================== File Upload Handling ====================

function setupFileUpload() {
  const uploadArea = document.getElementById("uploadArea");
  const fileInput = document.getElementById("fileInput");
  const browseBtn = document.getElementById("browseBtn");

  browseBtn.addEventListener("click", () => fileInput.click());

  fileInput.addEventListener("change", function (e) {
    handleFileSelect(this.files[0]);
  });

  // Drag and drop
  uploadArea.addEventListener("dragover", (e) => {
    e.preventDefault();
    uploadArea.classList.add("dragover");
  });

  uploadArea.addEventListener("dragleave", () => {
    uploadArea.classList.remove("dragover");
  });

  uploadArea.addEventListener("drop", (e) => {
    e.preventDefault();
    uploadArea.classList.remove("dragover");
    handleFileSelect(e.dataTransfer.files[0]);
  });
}

async function handleFileSelect(file) {
  if (!file) return;

  const uploadStatus = document.getElementById("uploadStatus");

  if (!file.name.endsWith(".txt")) {
    showUploadError("Only .txt files are supported");
    return;
  }

  if (file.size > 16 * 1024 * 1024) {
    showUploadError("File size exceeds 16MB limit");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  showLoading();

  try {
    const response = await fetch("/api/upload", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();

    if (data.success) {
      displaySingleResult(data);
      showUploadSuccess(`File "${file.name}" analyzed successfully`);
    } else {
      showUploadError(data.message);
    }
  } catch (error) {
    console.error("Upload error:", error);
    showUploadError("Error uploading file: " + error.message);
  } finally {
    hideLoading();
  }
}

function showUploadError(message) {
  const uploadStatus = document.getElementById("uploadStatus");
  uploadStatus.textContent = "❌ " + message;
  uploadStatus.className = "upload-status error";
}

function showUploadSuccess(message) {
  const uploadStatus = document.getElementById("uploadStatus");
  uploadStatus.textContent = "  " + message;
  uploadStatus.className = "upload-status success";
}

// ==================== Batch Analysis ====================

function setupBatchAnalysis() {
  // Already handled in event listeners
}

async function batchAnalyze() {
  const batchInput = document.getElementById("batchInput").value;

  if (!batchInput.trim()) {
    showError("Please enter some texts to analyze");
    return;
  }

  // Split by empty lines
  const texts = batchInput
    .split("\n\n")
    .map((text) => text.trim())
    .filter((text) => text.length > 0);

  if (texts.length === 0) {
    showError("Please enter valid texts separated by empty lines");
    return;
  }

  if (texts.length > 50) {
    showError("Maximum 50 texts can be analyzed at once");
    return;
  }

  await performAnalysis({ texts }, "batch");
}

// ==================== API Calls ====================

async function performAnalysis(payload, analysisType) {
  showLoading();
  document.getElementById("resultsSection").style.display = "block";

  try {
    let endpoint = "/api/analyze";
    let method = "POST";

    if (analysisType === "batch") {
      endpoint = "/api/batch";
    }

    const response = await fetch(endpoint, {
      method: method,
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();

    if (data.success) {
      if (analysisType === "single") {
        displaySingleResult(data);
      } else if (analysisType === "batch") {
        displayBatchResults(data);
      }
      clearErrorMessage();
    } else {
      showError(data.message);
    }
  } catch (error) {
    console.error("Analysis error:", error);
    showError("Error during analysis: " + error.message);
  } finally {
    hideLoading();
  }
}

// ==================== Result Display ====================

function displaySingleResult(data) {
  const singleResult = document.getElementById("singleResult");
  const batchResults = document.getElementById("batchResults");

  // Hide batch results
  batchResults.style.display = "none";
  singleResult.style.display = "block";

  const sentiment = data.sentiment;
  const scores = data.scores;

  // Update confidence - use absolute value of compound score (0 to 1)
  const confidence = Math.abs(scores.compound);
  const confidenceFill = document.getElementById("confidenceFill");
  const confidencePercent = document.getElementById("confidencePercent");

  confidenceFill.style.width = confidence * 100 + "%";
  confidencePercent.textContent = (confidence * 100).toFixed(1) + "%";

  // Display quick result in left column
  displayQuickResultInLeftColumn(sentiment, data.processed_text);

  // Create/update chart
  createSentimentChart(scores);

  // Create bar chart for component breakdown
  setTimeout(() => createComponentBarChart(scores), 100);

  // Update sentiment gauge
  setTimeout(() => updateSentimentGauge(scores.compound), 100);

  // Display key indicators
  setTimeout(() => displayKeyIndicators(scores), 100);
}

function displayQuickResultInLeftColumn(sentiment, processedText) {
  // Determine which tab is active and show appropriate left column result
  const activeTab = document
    .querySelector(".tab-btn.active")
    .getAttribute("data-tab");

  let leftResultDiv, sentimentDiv, preprocessDiv;

  if (activeTab === "text-input") {
    leftResultDiv = document.getElementById("leftColumnResult");
    sentimentDiv = document.getElementById("quickSentiment");
    preprocessDiv = document.getElementById("quickPreprocessed");
  } else if (activeTab === "file-upload") {
    leftResultDiv = document.getElementById("leftColumnFileResult");
    sentimentDiv = document.getElementById("quickFilesentiment");
    preprocessDiv = document.getElementById("quickFilePreprocessed");
  }

  if (leftResultDiv && sentimentDiv && preprocessDiv) {
    // Show the left column result
    leftResultDiv.style.display = "block";

    // Set sentiment with emoji
    let emoji = "😊";
    let color = "#10b981";
    if (sentiment === "negative") {
      emoji = "😞";
      color = "#ef4444";
    } else if (sentiment === "neutral") {
      emoji = "😐";
      color = "#f59e0b";
    }

    sentimentDiv.innerHTML = `
      <div style="font-size: 2.5em; margin-bottom: 10px;">${emoji}</div>
      <div style="font-size: 1.2em; font-weight: bold; color: ${color};">${sentiment.toUpperCase()}</div>
    `;

    // Set preprocessed text (truncated if too long)
    const truncated =
      processedText && processedText.length > 300
        ? processedText.substring(0, 300) + "..."
        : processedText || "N/A";
    preprocessDiv.textContent = truncated;
  }
}

function displayBatchResults(data) {
  const batchResults = document.getElementById("batchResults");
  const singleResult = document.getElementById("singleResult");

  // Hide single result
  singleResult.style.display = "none";
  batchResults.style.display = "block";

  // Display summary
  const summary = document.getElementById("batchSummary");
  const avgCompound = data.average_compound_score || 0;

  summary.innerHTML = `
        <p><strong>Total Texts Analyzed:</strong> ${data.count}</p>
        <p><strong>Positive:</strong> ${data.results.filter((r) => r.sentiment === "positive").length} | 
           <strong>Negative:</strong> ${data.results.filter((r) => r.sentiment === "negative").length} | 
           <strong>Neutral:</strong> ${data.results.filter((r) => r.sentiment === "neutral").length}</p>
        <p><strong>Average Compound Score:</strong> ${(typeof avgCompound === "number" ? avgCompound : 0).toFixed(3)}</p>
    `;

  // Display results list
  const resultsList = document.getElementById("batchResultsList");
  resultsList.innerHTML = "";

  data.results.forEach((result, index) => {
    const item = document.createElement("div");
    item.className = `batch-result-item ${result.sentiment}`;

    // Safely handle scores
    const scores = result.scores || {};
    const posScore = ((scores.positive || 0) * 100).toFixed(1);
    const negScore = ((scores.negative || 0) * 100).toFixed(1);

    item.innerHTML = `
            <div class="batch-result-item-text">
                <strong>Text ${index + 1}:</strong> ${result.text.substring(0, 100)}${result.text.length > 100 ? "..." : ""}
            </div>
            <div>
                <span class="batch-result-item-sentiment">${result.sentiment.toUpperCase()}</span>
                <span style="margin-left: 10px; color: #64748b;">
                    Positive: ${posScore}% | 
                    Negative: ${negScore}%
                </span>
            </div>
        `;
    resultsList.appendChild(item);
  });
}

function createSentimentChart(scores) {
  const ctx = document.getElementById("sentimentChart").getContext("2d");

  // Destroy existing chart
  if (currentChart) {
    currentChart.destroy();
  }

  currentChart = new Chart(ctx, {
    type: "doughnut",
    data: {
      labels: ["Positive", "Negative", "Neutral"],
      datasets: [
        {
          data: [scores.positive, scores.negative, scores.neutral],
          backgroundColor: [
            "rgba(16, 185, 129, 0.7)", // Green for positive
            "rgba(239, 68, 68, 0.7)", // Red for negative
            "rgba(245, 158, 11, 0.7)", // Orange for neutral
          ],
          borderColor: [
            "rgb(16, 185, 129)",
            "rgb(239, 68, 68)",
            "rgb(245, 158, 11)",
          ],
          borderWidth: 2,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          position: "bottom",
          labels: {
            padding: 20,
            font: {
              size: 12,
              weight: "bold",
            },
          },
        },
      },
    },
  });
}

// ==================== Additional Visualizations ====================

function createComponentBarChart(scores) {
  const barCanvasElement = document.getElementById("barChart");

  // Return if canvas doesn't exist
  if (!barCanvasElement) return;

  const ctx = barCanvasElement.getContext("2d");

  // Destroy existing chart if it exists
  if (window.barChartInstance) {
    window.barChartInstance.destroy();
  }

  window.barChartInstance = new Chart(ctx, {
    type: "bar",
    data: {
      labels: ["Positive", "Negative", "Neutral"],
      datasets: [
        {
          label: "Sentiment Scores",
          data: [
            (scores.positive * 100).toFixed(1),
            (scores.negative * 100).toFixed(1),
            (scores.neutral * 100).toFixed(1),
          ],
          backgroundColor: [
            "rgba(16, 185, 129, 0.8)", // Green
            "rgba(239, 68, 68, 0.8)", // Red
            "rgba(245, 158, 11, 0.8)", // Orange
          ],
          borderColor: [
            "rgb(16, 185, 129)",
            "rgb(239, 68, 68)",
            "rgb(245, 158, 11)",
          ],
          borderWidth: 2,
          borderRadius: 6,
        },
      ],
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      indexAxis: "y",
      scales: {
        x: {
          beginAtZero: true,
          max: 100,
          ticks: {
            callback: function (value) {
              return value + "%";
            },
          },
        },
      },
      plugins: {
        legend: {
          display: false,
        },
      },
    },
  });
}

function updateSentimentGauge(compoundScore) {
  const gaugeFill = document.getElementById("gaugeFill");
  const gaugeValue = document.getElementById("gaugeValue");

  if (!gaugeFill || !gaugeValue) return;

  // Convert compound score (-1 to 1) to percentage (0 to 100)
  const percentage = ((compoundScore + 1) / 2) * 100;

  // Update gauge fill width and position
  gaugeFill.style.width = percentage + "%";

  // Adjust position based on percentage
  if (percentage < 50) {
    gaugeFill.style.left = percentage + "%";
  } else {
    gaugeFill.style.left = percentage + "%";
  }

  // Update displayed value
  gaugeValue.textContent = compoundScore.toFixed(3);

  // Color code based on sentiment
  if (compoundScore > 0.5) {
    gaugeValue.style.color = "#10b981";
  } else if (compoundScore < -0.5) {
    gaugeValue.style.color = "#ef4444";
  } else {
    gaugeValue.style.color = "#f59e0b";
  }
}

function displayKeyIndicators(scores) {
  const indicatorsContent = document.getElementById("indicatorsContent");

  if (!indicatorsContent) return;

  // Determine dominant sentiment
  let dominantSentiment = "Neutral";
  let dominantValue = scores.neutral;

  if (scores.positive > dominantValue) {
    dominantSentiment = "Positive";
    dominantValue = scores.positive;
  }

  if (scores.negative > dominantValue) {
    dominantSentiment = "Negative";
    dominantValue = scores.negative;
  }

  // Calculate subjectivity (opposite of neutrality)
  const subjectivity = 1 - scores.neutral;

  // Create indicator items
  const indicators = [
    {
      label: "Primary Sentiment",
      value: dominantSentiment,
      icon:
        dominantSentiment === "Positive"
          ? "😊"
          : dominantSentiment === "Negative"
            ? "😞"
            : "😐",
    },
    {
      label: "Positivity",
      value: (scores.positive * 100).toFixed(1) + "%",
      icon: "📈",
    },
    {
      label: "Negativity",
      value: (scores.negative * 100).toFixed(1) + "%",
      icon: "📉",
    },
    {
      label: "Neutrality",
      value: (scores.neutral * 100).toFixed(1) + "%",
      icon: "➡️",
    },
    {
      label: "Subjectivity",
      value: (subjectivity * 100).toFixed(1) + "%",
      icon: "💭",
    },
    {
      label: "Compound Score",
      value: scores.compound.toFixed(3),
      icon: "⚖️",
    },
  ];

  // Build HTML
  indicatorsContent.innerHTML = indicators
    .map(
      (indicator) => `
    <div class="indicator-item">
      <span style="font-size: 1.6em; margin-bottom: 4px; display: block;">${indicator.icon}</span>
      <span class="indicator-label">${indicator.label}</span>
      <span class="indicator-value">${indicator.value}</span>
    </div>
  `,
    )
    .join("");
}

// ==================== Utility Functions ====================

function showLoading() {
  document.getElementById("loadingSpinner").style.display = "block";
  document.getElementById("singleResult").style.display = "none";
  document.getElementById("batchResults").style.display = "none";
  document.getElementById("errorMessage").style.display = "none";
}

function hideLoading() {
  document.getElementById("loadingSpinner").style.display = "none";
}

function showError(message) {
  const errorDiv = document.getElementById("errorMessage");
  errorDiv.textContent = "❌ " + message;
  errorDiv.style.display = "block";
}

function clearErrorMessage() {
  document.getElementById("errorMessage").style.display = "none";
}

// ==================== Keyboard Shortcuts ====================

document.addEventListener("keydown", function (e) {
  // Ctrl/Cmd + Enter to analyze in text input tab
  if ((e.ctrlKey || e.metaKey) && e.key === "Enter") {
    const textInput = document.getElementById("textInput");
    if (document.activeElement === textInput) {
      analyzeText();
    }
  }
});
