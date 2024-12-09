function loadPetDetail(petID) {
    document.getElementById('pet-detail-container').style.display = 'block';
    document.getElementById('pet-detail-iframe').src = "/dashboard/pet_detail/" + petID + "/";
}