document.addEventListener("DOMContentLoaded", function () {
  const toastContainer = document.querySelector(".toast-container");

  document.querySelectorAll(".toast-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      const product = btn.getAttribute("data-product") || "Item";

      const toast = document.createElement("div");
      toast.className = "toast align-items-center text-bg-success border-0 show";
      toast.role = "alert";
      toast.ariaLive = "assertive";
      toast.ariaAtomic = "true";
      toast.innerHTML = `
        <div class="d-flex">
          <div class="toast-body">✅ ${product} added to cart!</div>
          <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
        </div>`;

      toastContainer.appendChild(toast);

      setTimeout(() => {
        toast.classList.remove("show");
        toast.classList.add("hide");
        setTimeout(() => toast.remove(), 500);
      }, 3000);
    });
  });
});
