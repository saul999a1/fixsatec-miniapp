// Reemplaza con tu ID de zona de Monetag
const ZONE_ID = 'TU_ZONE_ID'; 

function showReward() {
  Monetag.rewarded({
    zoneId: ZONE_ID,
    onComplete: () => alert('¡Gracias! Has apoyado el canal.')
  });
}

// Inicia Monetag
Monetag.init({ zoneId: ZONE_ID });
