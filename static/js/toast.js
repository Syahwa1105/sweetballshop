let toastTimeout; 

function showToast(title, message, type = "info") {
  const toast = document.getElementById("toast-component");
  const toastTitle = document.getElementById("toast-title");
  const toastMessage = document.getElementById("toast-message");
  const toastIcon = document.getElementById("toast-icon");

  const colors = {
    success: "border-green-400 bg-green-100 text-green-700",
    error: "border-red-400 bg-red-100 text-red-700",
    info: "border-blue-400 bg-blue-100 text-blue-700",
  };

  const icons = {
    success: "✅",
    error: "❌",
    info: "ℹ️",
  };

  
  clearTimeout(toastTimeout);
  toast.classList.add("opacity-0", "translate-y-64");

  
  toast.className = `fixed bottom-8 right-8 p-4 px-8 rounded-xl shadow-xl z-50 flex items-center gap-4 border ${colors[type]} opacity-0 translate-y-64 transition-all duration-300`;
  toastTitle.textContent = title;
  toastMessage.textContent = message;
  toastIcon.textContent = icons[type];

  // Tampilkan dengan animasi
  setTimeout(() => {
    toast.classList.remove("opacity-0", "translate-y-64");
  }, 50);

  // Sembunyikan setelah 2.5 detik
  toastTimeout = setTimeout(() => {
    toast.classList.add("opacity-0", "translate-y-64");
  }, 2500);
}
