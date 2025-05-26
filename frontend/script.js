const api = "http://127.0.0.1:8000";

document.addEventListener("DOMContentLoaded", () => {
  loadProducts();
  loadSuppliers();

  document.getElementById("product-form").addEventListener("submit", async e => {
    e.preventDefault();
    const name = document.getElementById("product-name").value;
    const quantity = parseInt(document.getElementById("product-quantity").value);
    const supplier_id = parseInt(document.getElementById("product-supplier").value);

    const res = await fetch(`${api}/products/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, quantity, supplier_id })
    });

    if (res.ok) {
      loadProducts();
      e.target.reset();
    }
  });

  document.getElementById("supplier-form").addEventListener("submit", async e => {
    e.preventDefault();
    const name = document.getElementById("supplier-name").value;
    const contact = document.getElementById("supplier-contact").value;

    const res = await fetch(`${api}/suppliers/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, contact })
    });

    if (res.ok) {
      loadSuppliers();
      e.target.reset();
    }
  });
});

async function loadProducts() {
  const res = await fetch(`${api}/products/`);
  const products = await res.json();
  const list = document.getElementById("product-list");
  list.innerHTML = "";
  products.forEach(p => {
    const item = document.createElement("li");
    item.className = "bg-white p-2 rounded shadow";
    item.textContent = `${p.name} (Qty: ${p.quantity}, Supplier: ${p.supplier_id})`;
    list.appendChild(item);
  });
}

async function loadSuppliers() {
  const res = await fetch(`${api}/suppliers/`);
  const suppliers = await res.json();
  const list = document.getElementById("supplier-list");
  list.innerHTML = "";
  suppliers.forEach(s => {
    const item = document.createElement("li");
    item.className = "bg-white p-2 rounded shadow";
    item.textContent = `${s.name} (Contact: ${s.contact}) [ID: ${s.id}]`;
    list.appendChild(item);
  });
}
