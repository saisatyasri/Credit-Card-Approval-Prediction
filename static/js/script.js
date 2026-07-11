/* ======================================================
   CreditAI — Credit Card Approval Prediction
   Main JavaScript
   ====================================================== */

// ---- Income display formatter ----
function updateIncomeDisplay(value) {
  const el = document.getElementById('incomeDisplay');
  if (!el) return;
  const num = parseFloat(value);
  if (!isNaN(num) && num > 0) {
    el.textContent = '≈ ₹' + num.toLocaleString('en-IN');
  } else {
    el.textContent = '';
  }
}

// ---- Unemployed indicator ----
window.updateUnemployed = function(value) {
  const note = document.getElementById('employedNote');
  if (!note) return;
  const yrs = parseFloat(value);
  if (yrs === 0) {
    note.innerHTML = '<span class="text-warning"><i class="bi bi-exclamation-circle me-1"></i>Marked as unemployed</span>';
  } else {
    note.textContent = '';
  }
};

// ---- Select helper ----
window.setSelectValue = function(id, value) {
  const el = document.getElementById(id);
  if (!el) return;
  for (let i = 0; i < el.options.length; i++) {
    if (el.options[i].value === value) {
      el.selectedIndex = i;
      break;
    }
  }
};

// ---- Form submit — show loading state ----
function setupFormSubmit() {
  const form = document.getElementById('predictForm');
  const btn  = document.getElementById('submitBtn');
  if (!form || !btn) return;

  form.addEventListener('submit', function(e) {
    // Basic validation
    const age    = parseInt(document.getElementById('age')?.value || '0');
    const income = parseFloat(document.getElementById('income')?.value || '0');

    if (age < 18 || age > 75) {
      e.preventDefault();
      alert('Age must be between 18 and 75.');
      return;
    }
    if (income <= 0) {
      e.preventDefault();
      alert('Please enter a valid annual income.');
      return;
    }

    btn.disabled   = true;
    btn.innerHTML  = '<span class="spinner-border spinner-border-sm me-2"></span>Analyzing...';
  });
}

// ---- Scroll to result if present ----
function scrollToResult() {
  const result = document.getElementById('result-section');
  if (result) {
    setTimeout(() => {
      result.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }, 200);
  }
}

// ---- Animate progress bars on page load ----
function animateProgressBars() {
  document.querySelectorAll('.progress-bar[style*="width"]').forEach(bar => {
    const target = bar.style.width;
    bar.style.width = '0%';
    bar.style.transition = 'width 0.8s ease';
    setTimeout(() => { bar.style.width = target; }, 100);
  });
}

// ---- Init ----
document.addEventListener('DOMContentLoaded', function () {
  // Income formatter
  const incomeInput = document.getElementById('income');
  if (incomeInput) {
    incomeInput.addEventListener('input', () => updateIncomeDisplay(incomeInput.value));
    updateIncomeDisplay(incomeInput.value);
  }

  // Employed years note
  const empInput = document.getElementById('employed_years');
  if (empInput) {
    empInput.addEventListener('input', () => updateUnemployed(empInput.value));
    updateUnemployed(empInput.value);
  }

  setupFormSubmit();
  scrollToResult();
  animateProgressBars();
});
