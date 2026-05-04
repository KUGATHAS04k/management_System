function loadSales() {
  fetch("http://127.0.0.1:5000/sales")
    .then(res => res.json())
    .then(data => {
      let output = "";

      data.forEach(sale => {
        output += `
          <div style="border:1px solid gray; padding:10px; margin:10px;">
            <p><b>Date:</b> ${sale.date}</p>
            <p>Cash: ${sale.cash}</p>
            <p>Card: ${sale.card}</p>
            <p>Uber: ${sale.uber}</p>
            <p><b>Shift:</b> ${sale.shift}</p>
            <p><b>Staff:</b> ${sale.staff_id}</p>
          </div>
        `;
      });

      document.getElementById("sales").innerHTML = output;
    })
    .catch(err => {
      console.log(err);
      alert("Error loading sales");
    });
}

// auto load when page opens
loadSales();