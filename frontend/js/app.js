/**
 * BharatAgri AI — Main Application Router
 * Handles SPA navigation and page lifecycle.
 */

let currentPage = 'home';

const pageRenderers = {
    home: renderHomePage,
    login: renderLoginPage,
    register: renderRegisterPage,
    recommend: renderRecommendPage,
    dashboard: renderDashboardPage,
    chatbot: renderChatbotPage,
    profile: renderProfilePage
};

const pageInitializers = {
    register: initRegisterPage,
    recommend: initRecommendPage,
    dashboard: initDashboardPage
};

function navigate(page) {
    currentPage = page;
    renderCurrentPage();

    // Update nav active state
    document.querySelectorAll('.nav-link').forEach(link => {
        link.classList.remove('active');
        if (link.dataset.page === page) link.classList.add('active');
    });

    // Close mobile menu
    document.getElementById('navLinks').classList.remove('show');

    // Scroll to top
    window.scrollTo(0, 0);
}

function renderCurrentPage() {
    const renderer = pageRenderers[currentPage];
    if (renderer) {
        document.getElementById('app').innerHTML = renderer();

        // Run page initializer if exists
        const init = pageInitializers[currentPage];
        if (init) {
            setTimeout(init, 50);
        }
    }

    // Update nav text for current language
    updateNavText();
}

// Initialize on load
document.addEventListener('DOMContentLoaded', () => {
    // Set up auth UI
    updateAuthUI();

    // Render initial page
    renderCurrentPage();

    // Navbar scroll effect
    window.addEventListener('scroll', () => {
        const nav = document.getElementById('navbar');
        if (window.scrollY > 10) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });
});
