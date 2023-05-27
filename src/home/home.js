const createButton = document.querySelector('.create-button');
const searchInput = document.querySelector('.search-input');

createButton.addEventListener('click', () => {
  window.location.href = '../Patient/formPatient.html';
  localStorage.removeItem("updatePatient");
});

const list = document.querySelector("table tbody");

// Hàm lấy dữ liệu từ API
async function fetchData() {
  const response = await fetch("http://127.0.0.1:5000/patients");
  const data = await response.json();
  return data;
}

// Hàm xóa hết nội dung trong bảng
function clearTable() {
  list.innerHTML = "";
}

// Hàm tạo các dòng trong bảng từ dữ liệu
function createRows(data) {
  clearTable();
  data.forEach((item) => {
    const row = document.createElement("tr");
    row.innerHTML = `
        <td>
        <input type="text" class="name-input" value="${item.patient.name}">
      </td>
      <td>
        <input type="text" class="address-input" value="${item.patient.address}">
      </td>
      <td>
        <input type="text" class="phone-input" value="${item.patient.phone}">
      </td>
      <td>
        <input type="date" class="birthday-input" value="${item.patient.birthday}">
      </td>
      <td>
        <select class="gender-input">
          <option value="male" ${item.patient.gender === 'male' ? 'selected' : ''}>Male</option>
          <option value="female" ${item.patient.gender === 'female' ? 'selected' : ''}>Female</option>
          <option value="other" ${item.patient.gender === 'other' ? 'selected' : ''}>Other</option>
        </select>
      </td>
      <td>
        <button class="update" data-id="${item.patient.id}">Update</button>
      </td>
      <td>
        <button class="delete" data-id="${item.patient.id}">Delete</button>
      </td>
    `;
    row.querySelector(".update").addEventListener("click", () => {
      localStorage.setItem("updatePatient", JSON.stringify(item));
      window.location.href = '../Patient/formPatient.html';
    });
    list.appendChild(row);
  });
}

// Hàm thực hiện lấy dữ liệu và hiển thị trên bảng
async function getData() {
  try {
    const data = await fetchData();
    createRows(data);
  } catch (error) {
    console.log("Error:", error);
  }
}

// Gọi hàm để lấy dữ liệu khi trang được tải
getData();

// Xử lý sự kiện xóa bệnh nhân
list.addEventListener("click", async (event) => {
  if (event.target.classList.contains("delete")) {
    const button = event.target;
    const patientId = button.getAttribute("data-id");
    try {
      const response = await fetch(`http://127.0.0.1:5000/patients/${patientId}`, {
        method: "DELETE"
      });
      if (response.ok) {
        button.parentElement.parentElement.remove();
        console.log("Patient deleted successfully!");
      } else {
        console.log("Failed to delete patient.");
      }
    } catch (error) {
      console.log("Error:", error);
    }
  }
});

// Xử lý sự kiện tìm kiếm khi nhập liệu vào trường tìm kiếm
searchInput.addEventListener("input", async () => {
  const searchValue = searchInput.value.trim().toLowerCase();
  if (searchValue === "") {
    getData();
  } else {
    try {
      const data = await fetchData();
      const filteredData = data.filter((item) =>
        item.patient.name.toLowerCase().includes(searchValue)
      );
      createRows(filteredData);
    } catch (error) {
      console.log("Error:", error);
    }
  }
});
