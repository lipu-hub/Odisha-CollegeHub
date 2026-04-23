// Function to show college details in a popup
function showDetails(id) {
    const college = colleges.find(c => c.id === id);
    if (!college) return;

    const modal = document.getElementById("collegeModal");
    const detailsDiv = document.getElementById("modalDetails");

    detailsDiv.innerHTML = `
        <div style="text-align:center;">
            <img src="${college.image}" style="width:100%; max-height:250px; object-fit:cover; border-radius:10px;">
            <h2 style="margin-top:15px;">${college.name}</h2>
            <p>📍 ${college.location} | ⭐ ${college.rating}</p>
            <hr>
            <div style="text-align:left; padding:10px;">
                <p><strong>Fees:</strong> ${college.fees}</p>
                <p><strong>Average Package:</strong> ${college.avgPackage}</p>
                <p><strong>Rank:</strong> #${college.rank} in Odisha</p>
                <p><strong>NIRF Score:</strong> ${college.nirfScore}</p>
            </div>
            <button onclick="closeModal()" style="background:#ff4b4b; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; margin-top:10px;">Close</button>
        </div>
    `;
    modal.style.display = "block";
}

function closeModal() {
    document.getElementById("collegeModal").style.display = "none";
}

// Ensure your card rendering uses: 
// <button onclick="showDetails(${college.id})" class="view-btn">View Details</button>
