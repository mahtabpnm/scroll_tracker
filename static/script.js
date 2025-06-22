window.addEventListener("scroll", () => {
  const scrollTop = window.scrollY;
  const docHeight = document.documentElement.scrollHeight - window.innerHeight;
  const percent = Math.round((scrollTop / docHeight) * 100);
  document.getElementById("progress").style.width = percent + "%";
  document.getElementById("label").innerText = `Viewed: ${percent}%`;

  fetch("/get_tip", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ percent: percent })
  })
  .then(response => response.json())
  .then(data => {
    document.getElementById("tip-box").innerText = `Tip: ${data.tip}`;
  });
});
