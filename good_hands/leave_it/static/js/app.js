document.addEventListener("DOMContentLoaded", function() {
  /**
   * HomePage - Help section
   */
 class Help {
  constructor($el) {
    this.$el = $el;
    this.$buttonsContainer = $el.querySelector(".help--buttons");
    this.$slidesContainers = $el.querySelectorAll(".help--slides");
    this.currentSlide = this.$buttonsContainer.querySelector(".active").parentElement.dataset.id;
    this.init();
  }

  init() {
    this.events();
    this.initPagination(); // Inicjacja paginacji
  }

  events() {
    this.$buttonsContainer.addEventListener("click", (e) => {
      if (e.target.classList.contains("btn")) {
        this.changeSlide(e);
      }
    });

    this.$el.addEventListener("click", (e) => {
      if (
        e.target.classList.contains("btn") &&
        e.target.parentElement.parentElement.classList.contains("help--slides-pagination")
      ) {
        this.changePage(e);
      }
    });
  }

  changeSlide(e) {
    e.preventDefault();
    const $btn = e.target;

    // Buttons Active class change
    [...this.$buttonsContainer.children].forEach((btn) => btn.firstElementChild.classList.remove("active"));
    $btn.classList.add("active");

    // Current slide
    this.currentSlide = $btn.parentElement.dataset.id;

    // Slides active class change
    this.$slidesContainers.forEach((el) => {
      el.classList.remove("active");

      if (el.dataset.id === this.currentSlide) {
        el.classList.add("active");
      }
    });
  }

  changePage(e) {
    e.preventDefault();
    const page = e.target.dataset.page;

    console.log(page);
  }

  // Kod paginacji




//   initPagination() {
//      // Zbiera wszystkie elementy listy z klasą 'help--slides-items li'
//     const items = document.querySelectorAll('.help--slides-items li');
//
//     const itemsPerPage = 5; // liczba elementów na stronie
//     let currentPage = 1; // Zmienna przechowująca numer aktualnej strony
//
//     function showPage(page) {
//       console.log("Current page:", page); // Dodany console.log
//       items.forEach((item, index) => {
//         if (index >= (page - 1) * itemsPerPage && index < page * itemsPerPage) {
//           item.style.display = 'block';
//         } else {
//           item.style.display = 'none';
//         }
//       });
//     }
//
//     const pagination = document.querySelector('.help--slides-pagination');
//     pagination.addEventListener('click', function (event) {
//       if (event.target.tagName === 'A') {
//         currentPage = parseInt(event.target.getAttribute('data-page'));
//         console.log("New page:", currentPage); // Dodany console.log
//         showPage(currentPage);
//       }
//     });
//
//     showPage(currentPage);
//   }
//
}
  // Funkcja inicjująca paginację dla sekcji
function initPagination(sectionClass) {
  // Zbiera wszystkie sekcje odpowiadające podanej klasie
  const sections = document.querySelectorAll(`.${sectionClass}`);

  // Iteruje przez każdą znalezioną sekcję
  sections.forEach(section => {
    // Zbiera wszystkie elementy listy z klasą 'help--slides-items li' w obrębie danej sekcji
    const items = section.querySelectorAll('.help--slides-items li');
    // Określa liczbę elementów na stronie
    const itemsPerPage = 5;
    // Inicjalizuje zmienną przechowującą numer aktualnej strony
    let currentPage = 1;

    // Funkcja wyświetlająca odpowiednią stronę
    function showPage(page) {
      console.log(`[${sectionClass}] Current page:`, page); // Wyświetla numer aktualnej strony w konsoli
      // Iteruje przez każdy element i decyduje, czy powinien być widoczny czy nie, w zależności od numeru strony
      items.forEach((item, index) => {
        if (index >= (page - 1) * itemsPerPage && index < page * itemsPerPage) {
          item.style.display = 'block'; // Jeśli jest na odpowiedniej stronie, ustawia go na widoczny
        } else {
          item.style.display = 'none'; // Jeśli nie jest na odpowiedniej stronie, ustawia go na niewidoczny
        }
      });
    }

    // Zbiera paginację dla danej sekcji
    const pagination = section.querySelector('.help--slides-pagination');
    // Dodaje nasłuchiwanie na kliknięcie paginacji
    pagination.addEventListener('click', function (event) {
        event.preventDefault(); // Zatrzymuje domyślne zachowanie linku (przeładowanie strony)

      // Sprawdza, czy kliknięty element to link (A)
      if (event.target.tagName === 'A') {
        // Pobiera numer strony z atrybutu data-page klikniętego linku
        currentPage = parseInt(event.target.getAttribute('data-page'));
        console.log(`[${sectionClass}] New page:`, currentPage); // Wyświetla numer nowej strony w konsoli
        showPage(currentPage); // Wyświetla odpowiednią stronę

            // Usuwa klasę active od wszystkich elementów paginacji
        pagination.querySelectorAll('a').forEach(function(link) {
        link.classList.remove('active');
        });
          // Dodaje klasę active tylko do klikniętego linku
        event.target.classList.add('active');

      }
    });

    // Wyświetla pierwszą stronę przy inicjalizacji
    showPage(currentPage);


  });
}

// Inicjalizacja paginacji dla wszystkich sekcji
initPagination('help--slides'); // Organizacje Pozarządowe, Lokalne zbiórki

// initPagination('help--slides.active'); // Fundacje


const helpSection = document.querySelector(".help");
if (helpSection !== null) {
  new Help(helpSection);
}

  /**
   * Form Select
   */
  class FormSelect {
    constructor($el) {
      this.$el = $el;
      this.options = [...$el.children];
      this.init();
    }

    init() {
      this.createElements();
      this.addEvents();
      this.$el.parentElement.removeChild(this.$el);
    }

    createElements() {
      // Input for value
      this.valueInput = document.createElement("input");
      this.valueInput.type = "text";
      this.valueInput.name = this.$el.name;

      // Dropdown container
      this.dropdown = document.createElement("div");
      this.dropdown.classList.add("dropdown");

      // List container
      this.ul = document.createElement("ul");

      // All list options
      this.options.forEach((el, i) => {
        const li = document.createElement("li");
        li.dataset.value = el.value;
        li.innerText = el.innerText;

        if (i === 0) {
          // First clickable option
          this.current = document.createElement("div");
          this.current.innerText = el.innerText;
          this.dropdown.appendChild(this.current);
          this.valueInput.value = el.value;
          li.classList.add("selected");
        }

        this.ul.appendChild(li);
      });

      this.dropdown.appendChild(this.ul);
      this.dropdown.appendChild(this.valueInput);
      this.$el.parentElement.appendChild(this.dropdown);
    }

    addEvents() {
      this.dropdown.addEventListener("click", e => {
        const target = e.target;
        this.dropdown.classList.toggle("selecting");

        // Save new value only when clicked on li
        if (target.tagName === "LI") {
          this.valueInput.value = target.dataset.value;
          this.current.innerText = target.innerText;
        }
      });
    }
  }
  document.querySelectorAll(".form-group--dropdown select").forEach(el => {
    new FormSelect(el);
  });

  /**
   * Hide elements when clicked on document
   */
  document.addEventListener("click", function(e) {
    const target = e.target;
    const tagName = target.tagName;

    if (target.classList.contains("dropdown")) return false;

    if (tagName === "LI" && target.parentElement.parentElement.classList.contains("dropdown")) {
      return false;
    }

    if (tagName === "DIV" && target.parentElement.classList.contains("dropdown")) {
      return false;
    }

    document.querySelectorAll(".form-group--dropdown .dropdown").forEach(el => {
      el.classList.remove("selecting");
    });
  });

  /**
   * Switching between form steps
   */
  class FormSteps {
    constructor(form) {
      this.$form = form;
      this.$next = form.querySelectorAll(".next-step");
      this.$prev = form.querySelectorAll(".prev-step");
      this.$step = form.querySelector(".form--steps-counter span");
      this.currentStep = 1;

      this.$stepInstructions = form.querySelectorAll(".form--steps-instructions p");
      const $stepForms = form.querySelectorAll("form > div");
      this.slides = [...this.$stepInstructions, ...$stepForms];

      this.init();
    }

    /**
     * Init all methods
     */
    init() {
      this.events();
      this.updateForm();
    }

    /**
     * All events that are happening in form
     */
    events() {
      // Next step
      this.$next.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep++;
          this.updateForm();
        });
      });

      // Previous step
      this.$prev.forEach(btn => {
        btn.addEventListener("click", e => {
          e.preventDefault();
          this.currentStep--;
          this.updateForm();
        });
      });

      // Form submit
      this.$form.querySelector("form").addEventListener("submit", e => this.submit(e));
    }

    /**
     * Update form front-end
     * Show next or previous section etc.
     */
    updateForm() {
      this.$step.innerText = this.currentStep;

      // TODO: Validation

      this.slides.forEach(slide => {
        slide.classList.remove("active");

        if (slide.dataset.step == this.currentStep) {
          slide.classList.add("active");
        }
      });

      this.$stepInstructions[0].parentElement.parentElement.hidden = this.currentStep >= 6;
      this.$step.parentElement.hidden = this.currentStep >= 6;

      // TODO: get data from inputs and show them in summary
    }

    /**
     * Submit form
     *
     * TODO: validation, send data to server
     */
    submit(e) {
      e.preventDefault();
      this.currentStep++;
      this.updateForm();
    }
  }
  const form = document.querySelector(".form--steps");
  if (form !== null) {
    new FormSteps(form);
  }
});
