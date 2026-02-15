/**
 * BharatAgri AI — Authentication Module
 */
function isLoggedIn() {
    return !!localStorage.getItem('bharatagri_token');
}

function getUser() {
    const u = localStorage.getItem('bharatagri_user');
    return u ? JSON.parse(u) : null;
}

function setAuth(token, user) {
    localStorage.setItem('bharatagri_token', token);
    localStorage.setItem('bharatagri_user', JSON.stringify(user));
    updateAuthUI();
}

function logout() {
    localStorage.removeItem('bharatagri_token');
    localStorage.removeItem('bharatagri_user');
    updateAuthUI();
    navigate('home');
    showToast('Logged out successfully.');
}

function updateAuthUI() {
    const authBtns = document.getElementById('authButtons');
    const userMenu = document.getElementById('userMenu');
    const userNameText = document.getElementById('userNameText');

    if (isLoggedIn()) {
        const user = getUser();
        authBtns.classList.add('hidden');
        userMenu.classList.remove('hidden');
        userNameText.textContent = user?.name || 'User';
    } else {
        authBtns.classList.remove('hidden');
        userMenu.classList.add('hidden');
    }
}

async function handleLogin(e) {
    e.preventDefault();
    const email = document.getElementById('loginEmail').value;
    const password = document.getElementById('loginPassword').value;

    if (!email || !password) {
        showToast('Please fill in all fields', 'error');
        return;
    }

    try {
        const data = await apiLogin(email, password);
        if (data) {
            setAuth(data.access_token, data.user);
            showToast(`Welcome back, ${data.user.name}!`);
            navigate('recommend');
        }
    } catch (err) {
        // Error already shown by apiCall
    }
}

async function handleRegister(e) {
    e.preventDefault();
    const name = document.getElementById('regName').value;
    const email = document.getElementById('regEmail').value;
    const password = document.getElementById('regPassword').value;
    const state = document.getElementById('regState')?.value || '';

    if (!name || !email || !password) {
        showToast('Please fill in all required fields', 'error');
        return;
    }

    try {
        const data = await apiRegister(email, name, password, state);
        if (data) {
            setAuth(data.access_token, data.user);
            showToast(`Welcome to BharatAgri AI, ${data.user.name}!`);
            navigate('recommend');
        }
    } catch (err) {
        // Error already shown
    }
}
