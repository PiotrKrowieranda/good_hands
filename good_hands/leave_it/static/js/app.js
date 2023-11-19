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
            this.setupHelpButtons();

            // Inicjalizacja - załaduj dane dla domyślnej kategorii
            const defaultCategoryId = this.$buttonsContainer.querySelector('li').getAttribute('data-id');
            this.loadCategoryData(defaultCategoryId);
        }

        init() {
            this.events();
        }

        setupHelpButtons() {
            this.$buttonsContainer.querySelectorAll('li').forEach(button => {
                button.addEventListener('click', (event) => {
                    event.preventDefault();
                    const categoryId = button.getAttribute('data-id');
                    this.loadCategoryData(categoryId);
                });
            });
        }

        async loadCategoryData(categoryId) {
            console.log(`Loading data for category ID: ${categoryId}`);

            try {
                const response = await fetch(`/api/institutions/?category=${categoryId}`);
                const data = await response.json();

                console.log(`Received data for category ID: ${categoryId}`, data);

                // Dodaj dodatkowy log tutaj, aby sprawdzić, co jest przekazywane do createPagination
                console.log("Data being passed to createPagination:", data);


                this.createPagination(data, categoryId);
            } catch (error) {
                console.error("Error loading data:", error);
            }
        }

        // Funkcja do tworzenia paginacji
        createPagination(data, categoryId) {
            // Pobiera kontener slajdów dla konkretnej kategorii
            const slidesContainer = document.querySelector(`.help--slides[data-id='${categoryId}'] .help--slides-items`);

            // Pobiera kontener paginacji dla konkretnej kategorii
            const paginationContainer = document.querySelector(`.help--slides[data-id='${categoryId}'] .help--slides-pagination`);

            // Określa liczbę elementów na stronie
            const itemsPerPage = 5;
            let currentPage = 1;

            // Funkcja wyświetlająca odpowiednią stronę
            function showPage(page) {
                console.log(`[${categoryId}] Current page:`, page);
                paginationContainer.innerHTML = "";

                // Oblicza ilość stron na podstawie ilości danych i elementów na stronie
                const pages = Math.ceil(data.length / itemsPerPage);

                // Iteruje przez wszystkie strony i tworzy odpowiednie elementy paginacji
                for (let i = 1; i <= pages; i++) {
                    // Tworzy nowy element listy dla każdej strony
                    const paginationItem = document.createElement("li");
                    // Ustawia treść elementu listy jako numer strony i dodaje atrybut danych z numerem strony
                    paginationItem.innerHTML = `<a href="#" class="btn btn--small btn--without-border" data-page="${i}">${i}</a>`;
                    // Dodaje stworzony element do kontenera paginacji
                    paginationContainer.appendChild(paginationItem);
                }

                // Dodaje nasłuchiwanie na kliknięcie paginacji
                paginationContainer.addEventListener('click', function (event) {
                    event.preventDefault();

                    // Sprawdza, czy kliknięty element to link (A)
                    if (event.target.tagName === 'A') {
                        // Pobiera numer strony z atrybutu data-page klikniętego linku
                        currentPage = parseInt(event.target.getAttribute('data-page'));
                        console.log(`[${categoryId}] New page:`, currentPage);
                        // Wyświetla odpowiednią stronę
                        showPage(currentPage);
                    }
                });

                // Czyści istniejące dane w kontenerze slajdów
                slidesContainer.innerHTML = "";
                // Określa indeksy początkowy i końcowy dla danych na danej stronie
                const startIndex = (currentPage - 1) * itemsPerPage;
                const endIndex = startIndex + itemsPerPage;

                // Iteruje przez dane na danej stronie i dodaje je do kontenera slajdów
                data.slice(startIndex, endIndex).forEach((item) => {
                    const slideItem = document.createElement("li");
                    slideItem.innerHTML = `
                    <div class="col">
                        <div class="title">${item.name}</div>
                        <div class="subtitle">${item.description}</div>
                    </div>
                    <div class="col"><div class="text">${item.details}</div></div>
                `;
                    slidesContainer.appendChild(slideItem);
                });
            }

            // Inicjalizuje paginację dla danych
            showPage(currentPage);
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
    }

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
    document.addEventListener("click", function (e) {
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
        }
    }
});
