/**
 * BharatAgri AI — API Client
 * Handles all backend communication.
 */
const API_BASE = window.location.origin;

async function apiCall(endpoint, options = {}) {
    const token = localStorage.getItem('bharatagri_token');
    const headers = { 'Content-Type': 'application/json', ...options.headers };
    if (token) headers['Authorization'] = `Bearer ${token}`;

    try {
        const resp = await fetch(`${API_BASE}${endpoint}`, {
            ...options,
            headers
        });
        if (resp.status === 401) {
            localStorage.removeItem('bharatagri_token');
            localStorage.removeItem('bharatagri_user');
            updateAuthUI();
            showToast('Session expired. Please login again.', 'error');
            navigate('login');
            return null;
        }
        const data = await resp.json();
        if (!resp.ok) {
            throw new Error(data.detail || 'Something went wrong');
        }
        return data;
    } catch (err) {
        if (err.message !== 'Failed to fetch') {
            showToast(err.message, 'error');
        }
        throw err;
    }
}

// Auth API
async function apiRegister(email, name, password, state) {
    return apiCall('/api/auth/register', {
        method: 'POST',
        body: JSON.stringify({ email, name, password, state })
    });
}

async function apiLogin(email, password) {
    return apiCall('/api/auth/login', {
        method: 'POST',
        body: JSON.stringify({ email, password })
    });
}

async function apiGetProfile() {
    return apiCall('/api/auth/me');
}

// Reference API
async function apiGetStates() {
    return apiCall('/api/reference/states');
}

async function apiGetDistricts(state) {
    return apiCall(`/api/reference/districts/${encodeURIComponent(state)}`);
}

async function apiGetSoilTypes(state) {
    return apiCall(`/api/reference/soil-types/${encodeURIComponent(state)}`);
}

async function apiGetClimate(state) {
    return apiCall(`/api/reference/climate/${encodeURIComponent(state)}`);
}

async function apiGetSeasons() {
    return apiCall('/api/reference/seasons');
}

// Prediction API
async function apiFullPrediction(data) {
    return apiCall('/api/predict/full', {
        method: 'POST',
        body: JSON.stringify(data)
    });
}

async function apiGetHistory() {
    return apiCall('/api/predict/history');
}

// Chatbot API
async function apiChatMessage(message, language, context) {
    return apiCall('/api/chatbot/message', {
        method: 'POST',
        body: JSON.stringify({ message, language, context })
    });
}

// Utility
function showToast(msg, type = 'success') {
    const toast = document.getElementById('toast');
    const toastMsg = document.getElementById('toastMsg');
    toastMsg.textContent = msg;
    toast.className = `toast ${type}`;
    setTimeout(() => { toast.className = 'toast hidden'; }, 3500);
}

function showLoading(text) {
    document.getElementById('loadingText').textContent = text || t('loading');
    document.getElementById('loadingOverlay').classList.remove('hidden');
}

function hideLoading() {
    document.getElementById('loadingOverlay').classList.add('hidden');
}

// Admin API (uses X-Admin-Key header)
async function adminCall(endpoint) {
    const key = sessionStorage.getItem('bharatagri_admin_key');
    if (!key) throw new Error('No admin key');
    const resp = await fetch(`${API_BASE}${endpoint}`, {
        headers: { 'X-Admin-Key': key }
    });
    if (resp.status === 403) throw new Error('Invalid admin key');
    if (!resp.ok) throw new Error('Request failed');
    return resp.json();
}

async function apiAdminStats() { return adminCall('/api/admin/stats'); }
async function apiAdminUsers() { return adminCall('/api/admin/users'); }
async function apiAdminPredictions() { return adminCall('/api/admin/predictions'); }
async function apiAdminChats() { return adminCall('/api/admin/chats'); }
