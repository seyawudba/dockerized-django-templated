(() => {
  const topSchools = [
    "Primary Schools In Lagos/Ogun",
    "Secondary Schools In Ikeja and Maryland",
    "Secondary Schools In Lagos/Ogun",
    "Sixth Form Colleges In Lagos",
    "Top Secondary Schools In Ajah",
    "Secondary Schools In Alimosho",
    "Top Secondary Schools In Abidan",
    "Top Secondary Schools In Abuja",
    "Top Primary Schools In Lekki and Victoria Island",
    "Secondary Schools In Port Harcourt",
  ];

  document.addEventListener("DOMContentLoaded", (e) => {
    createPopularList();
    createFeaturedList();
    toogleNav();
  });
  function toogleNav() {
    const menu = document.querySelector(".__menu");
    const btn = document.querySelector(".__searchdown-trigger");
    console.log(menu);
    const dropdown = document.querySelector(".__dropdown");
    const searchButton = document.querySelector(".__search-forsearch_wrapper");
    const dropdownSearch = document.querySelector(".__dropdown-forsearch");
    menu.addEventListener("click", (e) => {
      dropdown.classList.toggle("show");
      dropdownSearch.classList.remove("show");
      searchButton.classList.remove("show");
    });
    btn.addEventListener("click", (e) => {
      searchButton.classList.toggle("show");
      dropdownSearch.classList.toggle("show");
      dropdown.classList.remove("show");

      console.log(searchButton.classList);
    });
  }

  function createPopularList() {
    const popularSchoolList = document.querySelector(".__pop-schools_list");

    topSchools.map((school) => {
      const div = document.createElement("div");
      div.className = "__pop-school_card card";
      const p = document.createElement("p");
      p.textContent = school;
      const img = document.createElement("img");
      img.src =
        "https://schoolscompass.com.ng/themes/front/asset/Group 36766.svg";
      img.alt = "arrow";
      img.classList.add("__card-arrow");
      div.append(p);
      div.append(img);
      console.log(div);
      popularSchoolList.append(div);
    });
  }
  function createFeaturedList() {
    const featuredSchoolsList = document.querySelector(
      ".__featured-schools_list"
    );

    Array.from({ length: 10 }).map((_, index) => {
      featuredSchoolsList.innerHTML += `<div class="__featured-school card">
          <div class="card-image">
            <img src="assets/gridimage${index + 1}.jpg" />
          </div>
          <div class="card-content">
            <p class="__rating_text">1 Review</p>
            <div class="__ratings">
              <p class="__rating_text">5</p>
              <div class="__ratings-icon">
                
                <i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i><i class="fa-solid fa-star"></i>
              </div>
            </div>
            <div>
              <span class="__rating_text"
                >3
               <i class="fa-solid fa-thumbs-up"></i>
            </div>
          </div>
        </div>`;
    });
  }
})();
