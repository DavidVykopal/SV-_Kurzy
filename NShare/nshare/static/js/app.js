document.addEventListener("DOMContentLoaded", () => {
  // Existing copy button functionality
  const copyButtons = document.querySelectorAll("[data-copy]");
  copyButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const text = btn.getAttribute("data-copy");
      if (!text) return;
      navigator.clipboard?.writeText(text).then(() => {
        btn.textContent = "Copied";
        setTimeout(() => (btn.textContent = "Copy link"), 1500);
      });
    });
  });

  // Notice board functionality
  const editBtn = document.getElementById("edit-notice-btn");
  const saveBtn = document.getElementById("save-notice-btn");
  const cancelBtn = document.getElementById("cancel-notice-btn");
  const display = document.getElementById("notice-display");
  const editor = document.getElementById("notice-editor");
  const textarea = document.getElementById("notice-textarea");

  if (editBtn && editor && display && textarea) {
    let originalText = "";

    editBtn.addEventListener("click", () => {
      originalText = textarea.value;
      display.style.display = "none";
      editor.style.display = "block";
      editBtn.style.display = "none";
      textarea.focus();
    });

    cancelBtn.addEventListener("click", () => {
      textarea.value = originalText;
      display.style.display = "block";
      editor.style.display = "none";
      editBtn.style.display = "inline-flex";
    });

    saveBtn.addEventListener("click", async () => {
      const newText = textarea.value;
      try {
        const response = await fetch("/api/notice", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text: newText }),
        });

        if (response.ok) {
          const data = await response.json();
          display.innerHTML = data.text ? escapeHtml(data.text) : '<em>No notices</em>';
          display.style.display = "block";
          editor.style.display = "none";
          editBtn.style.display = "inline-flex";
        } else {
          alert("Failed to save notice board");
        }
      } catch (error) {
        console.error("Error saving notice:", error);
        alert("Error saving notice board");
      }
    });
  }

  function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Delete file functionality
  const deleteButtons = document.querySelectorAll('.btn-delete');
  deleteButtons.forEach(btn => {
    btn.addEventListener('click', async function(e) {
      e.preventDefault();
      const path = this.getAttribute('data-path');
      const name = this.getAttribute('data-name');

      if (!confirm(`Are you sure you want to delete "${name}"?`)) {
        return;
      }

      try {
        const response = await fetch(`/api/delete?path=${encodeURIComponent(path)}`, {
          method: 'DELETE',
        });

        if (response.ok) {
          // Reload the page to show updated file list
          window.location.reload();
        } else {
          alert('Failed to delete file');
        }
      } catch (error) {
        console.error('Error deleting file:', error);
        alert('Error deleting file');
      }
    });
  });
});
