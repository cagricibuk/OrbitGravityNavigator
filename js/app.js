document.addEventListener('DOMContentLoaded', function() {
  loadCelestialBodies();
});

function loadCelestialBodies() {
  fetch('data/celestialBodies.json')
      .then(response => response.json())
      .then(data => {
          const celestialBodies = data.celestialBodies;

          const originSelect = document.getElementById('origin');
          const destinationSelect = document.getElementById('destination');

          celestialBodies.forEach(body => {
              // Gezegenler için option oluştur
              let option1 = document.createElement('option');
              let option2 = document.createElement('option');

              option1.value = body.name;
              option1.textContent = body.name;
              option2.value = body.name;
              option2.textContent = body.name;

              originSelect.appendChild(option1);
              destinationSelect.appendChild(option2);
          });
      })
      .catch(error => console.error('Error:', error));
}

// Plot ve Reset butonlarına fonksiyon ekle
document.getElementById('plot-btn').addEventListener('click', function() {
  const origin = document.getElementById('origin').value;
  const destination = document.getElementById('destination').value;
  const initialOrbit = document.getElementById('initial-orbit').value;
  const finalOrbit = document.getElementById('final-orbit').value;
  const departureYear = document.getElementById('departure-year').value;
  const departureDay = document.getElementById('departure-day').value;
  const transferType = document.getElementById('transfer-type').value;

  // Burada deltaV ve diğer hesaplamaları ekleyebilirsin
  alert(`Origin: ${origin}, Destination: ${destination}, Initial Orbit: ${initialOrbit} km, Final Orbit: ${finalOrbit} km, Earliest Departure: Year ${departureYear}, Day ${departureDay}, Transfer Type: ${transferType}`);
});

document.getElementById('reset-btn').addEventListener('click', function() {
  document.getElementById('origin').selectedIndex = 0;
  document.getElementById('destination').selectedIndex = 0;
  document.getElementById('initial-orbit').value = 100;
  document.getElementById('final-orbit').value = 100;
  document.getElementById('departure-year').value = 1;
  document.getElementById('departure-day').value = 1;
  document.getElementById('transfer-type').selectedIndex = 0;
});
