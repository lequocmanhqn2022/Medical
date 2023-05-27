const updatePatient = localStorage.getItem("updatePatient");
const patientForm = document.getElementById('patients');

if(updatePatient){
  const updatePatientOb = JSON.parse(updatePatient);
  const name = document.getElementById('name');
  const address = document.getElementById('address');
  const phone = document.getElementById('phone');
  const birthday = document.getElementById('birthday');
  const gender = document.getElementById('gender');

  name.value = updatePatientOb.patient.name;
  address.value = updatePatientOb.patient.address;
  phone.value = updatePatientOb.patient.phone;
  birthday.value = updatePatientOb.patient.birthday;
  gender.value = updatePatientOb.patient.gender;

  document.querySelector(".header > h1").textContent = "Update Patient";
  document.querySelector(".form-group > button").textContent = "Update";
}

patientForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  const name = document.getElementById('name').value;
  const address = document.getElementById('address').value;
  const phone = document.getElementById('phone').value;
  const birthday = document.getElementById('birthday').value;
  const gender = document.getElementById('gender').value;

  const patientData = {
    name: name,
    address: address,
    phone: phone,
    birthday: birthday,
    gender: gender
  };

  try {
    const response = await fetch(!updatePatient ? 'http://127.0.0.1:5000/patients' : `http://127.0.0.1:5000/patients/${JSON.parse(updatePatient).patient.id}`, {
      method: !updatePatient ? 'POST' : 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ patients: patientData })
    });

    if (response.ok) {
      const data = await response.json();
      console.log(data.message); 
      console.log(data.patients);
      window.location.href = '../home/home.html';
    } else {
      console.log('Error:', response.statusText);
    }
  } catch (error) {
    console.log('Error:', error);
  }
});
