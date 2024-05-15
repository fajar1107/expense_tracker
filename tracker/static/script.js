// script.js

// Function to toggle edit button
function toggleEditButton() {
    var actions = document.querySelectorAll('.actions');
    var editButton = document.querySelector('.edit-btn');
  
    actions.forEach(function(action) {
      if (action.style.display === "none") {
        action.style.display = "table-cell"; // Show the actions
        editButton.style.backgroundColor = "#90D26D"; // Change button color to white
      } else {
        action.style.display = "none"; // Hide the actions
        editButton.style.backgroundColor = ""; // Revert button color to default
      }
    });
  }
  
  // Function to filter table
  function filterTable() {
      var selectedYear = document.getElementById("year").value;
      var selectedMonth = document.getElementById("month").value.toLowerCase();
    console.log("Selected Month:", selectedMonth);
    console.log("Selected Year:", selectedYear);
    var tableRows = document.querySelectorAll("table tr");
  
    var filterButton = document.getElementById("filter-btn");
    var unfilterButton = document.getElementById("unfilter-btn");
  
    // Check if selected month and year are valid
    if (selectedMonth === 'all' && selectedYear === 'all') {
      alert("Please select a valid month and year.");
      return;
    }
  
    tableRows.forEach(function(row, index) {
        // Iterate over each table row
      // Display header row
      if (index === 0) {
        row.style.display = "";
      } else {
        // Handle data rows
        var rowDateStr = row.children[0].textContent.trim(); // Get the date string and remove leading/trailing whitespaces
        if (row.children.length > 0) {
          var rowDate = new Date(rowDateStr); // Parse the date string
          try {
            if (isNaN(rowDate.getTime())) {
              console.error("Invalid date format:", rowDateStr, "Row content:", row.textContent.trim());
              return; // Skip processing if date parsing fails
            }
            var rowMonth = ("0" + (rowDate.getMonth() + 1)).slice(-2); // Extract the month (zero-padded)
            var rowYear = rowDate.getFullYear().toString(); // Extract the year
  
            // Show row if it matches the selected month and year, or if all months and years are selected
            if ((selectedMonth === 'all' || selectedMonth === rowMonth) && (selectedYear === 'all' || selectedYear === rowYear)) {
              row.style.display = ""; // Show row
            } else {
              row.style.display = "none"; // Hide row
            }
          } catch (error) {
            console.error("Error parsing date:", rowDateStr, "Row content:", row.textContent.trim());
          }
        }
      }
    });
  
    // Toggle visibility of filter and unfilter buttons
    if (selectedMonth !== 'all' || selectedYear !== 'all') {
        unfilterButton.style.display = ""; // Show unfilter button
        filterButton.style.display = "none"; // Hide filter button
    } else {
      filterButton.style.display = ""; // Show filter button
      unfilterButton.style.display = "none"; // Hide unfilter button
    }
  }
  
  // Function to unfilter table
  function unfilterTable() {
    var tableRows = document.querySelectorAll("table tr");
  
    tableRows.forEach(function(row, index) {
      if (index !== 0) { // Skip the header row
        row.style.display = ""; // Show all rows
      }
    });
  
    // Toggle visibility of filter and unfilter buttons
    document.getElementById("filter-btn").style.display = ""; // Show filter button
    document.getElementById("unfilter-btn").style.display = "none"; // Hide unfilter button
  }
  
  // Function to show statement form
  function downloadStatement() {
    // Show the form for selecting start and end dates
    document.getElementById("statement-form").style.display = "block";
  }
  