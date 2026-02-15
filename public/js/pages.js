/**
 * BharatAgri AI — Page Renderers
 * All SPA page templates and interactions.
 */

// ======================== HOME PAGE ========================
function renderHomePage() {
    return `
    <section class="hero fade-in">
        <div class="hero-badge">${t('hero_badge')}</div>
        <h1>${t('hero_title')}</h1>
        <p>${t('hero_subtitle')}</p>
        <div class="hero-actions">
            <button class="btn btn-primary btn-lg" onclick="${isLoggedIn() ? "navigate('recommend')" : "navigate('register')"}">${t('get_started')} →</button>
            <button class="btn btn-outline btn-lg" onclick="document.querySelector('.features-grid').scrollIntoView({behavior:'smooth'})">${t('learn_more')}</button>
        </div>
    </section>

    <div class="stats-strip fade-in">
        <div class="stat-item"><div class="stat-number">16</div><div class="stat-label">${t('stat_states')}</div></div>
        <div class="stat-item"><div class="stat-number">25</div><div class="stat-label">${t('stat_crops')}</div></div>
        <div class="stat-item"><div class="stat-number">3</div><div class="stat-label">${t('stat_models')}</div></div>
    </div>

    <div class="features-grid">
        <div class="feature-card card-elevated fade-in">
            <span class="feature-icon">🌾</span>
            <h3>${t('feat_crop_title')}</h3>
            <p>${t('feat_crop_desc')}</p>
        </div>
        <div class="feature-card card-elevated fade-in">
            <span class="feature-icon">📊</span>
            <h3>${t('feat_yield_title')}</h3>
            <p>${t('feat_yield_desc')}</p>
        </div>
        <div class="feature-card card-elevated fade-in">
            <span class="feature-icon">⚡</span>
            <h3>${t('feat_risk_title')}</h3>
            <p>${t('feat_risk_desc')}</p>
        </div>
        <div class="feature-card card-elevated fade-in">
            <span class="feature-icon">🌐</span>
            <h3>${t('feat_multi_title')}</h3>
            <p>${t('feat_multi_desc')}</p>
        </div>
        <div class="feature-card card-elevated fade-in">
            <span class="feature-icon">🤖</span>
            <h3>${t('feat_chat_title')}</h3>
            <p>${t('feat_chat_desc')}</p>
        </div>
        <div class="feature-card card-elevated fade-in">
            <span class="feature-icon">🗺️</span>
            <h3>${t('feat_data_title')}</h3>
            <p>${t('feat_data_desc')}</p>
        </div>
    </div>

    <div class="footer">
        <p>BharatAgri AI © 2024 — Intelligent Crop & Yield Advisory System</p>
        <p style="margin-top:8px">Built for Indian farmers 🇮🇳 | <a href="#" onclick="navigate('recommend')">Get Recommendations</a></p>
    </div>
    `;
}

// ======================== LOGIN PAGE ========================
function renderLoginPage() {
    return `
    <div class="auth-container fade-in">
        <div class="auth-card card">
            <h2 class="auth-title">${t('login_title')}</h2>
            <p class="auth-subtitle">${t('login_sub') || 'Sign in to access your personalized dashboard.'}</p>
            <form onsubmit="handleLogin(event)">
                <div class="form-group">
                    <label class="form-label">${t('email')}</label>
                    <input type="email" id="loginEmail" class="form-input" placeholder="farmer@example.com" required>
                </div>
                <div class="form-group">
                    <label class="form-label">${t('password')}</label>
                    <input type="password" id="loginPassword" class="form-input" placeholder="••••••••" required>
                </div>
                <button type="submit" class="btn btn-primary w-full">${t('login')}</button>
            </form>
            <div class="auth-footer">
                ${t('dont_have_account') || "Don't have an account?"} <a href="#" onclick="navigate('register')">${t('signup')}</a>
            </div>
        </div>
    </div>
    `;
}

// ======================== REGISTER PAGE ========================
function renderRegisterPage() {
    return `
    <div class="auth-container fade-in">
        <div class="auth-card card">
            <h2 class="auth-title">${t('register_title')}</h2>
            <p class="auth-subtitle">${t('register_sub') || 'Join BharatAgri AI for smart farming insights.'}</p>
            <form onsubmit="handleRegister(event)">
                <div class="form-group">
                    <label class="form-label">${t('name')}</label>
                    <input type="text" id="regName" class="form-input" placeholder="Ram Kumar" required>
                </div>
                <div class="form-group">
                    <label class="form-label">${t('email')}</label>
                    <input type="email" id="regEmail" class="form-input" placeholder="farmer@example.com" required>
                </div>
                <div class="form-group">
                    <label class="form-label">${t('password')}</label>
                    <input type="password" id="regPassword" class="form-input" placeholder="••••••••" required minlength="6">
                </div>
                <div class="form-group">
                    <label class="form-label">${t('select_state')}</label>
                    <select id="regState" class="form-select"><option value="">-- Optional --</option></select>
                </div>
                <button type="submit" class="btn btn-primary w-full">${t('signup')}</button>
            </form>
            <div class="auth-footer">
                ${t('already_have_account') || 'Already have an account?'} <a href="#" onclick="navigate('login')">${t('login')}</a>
            </div>
        </div>
    </div>
    `;
}

// After render: populate state dropdown
async function initRegisterPage() {
    try {
        const data = await apiGetStates();
        const sel = document.getElementById('regState');
        if (sel && data?.states) {
            data.states.forEach(s => {
                sel.innerHTML += `<option value="${s}">${s}</option>`;
            });
        }
    } catch (e) { }
}

// ======================== RECOMMEND (ADVISORY) PAGE ========================
let lastPredictionResult = null;
let formData = {};

function renderRecommendPage() {
    if (!isLoggedIn()) {
        return `<div class="page page-narrow text-center fade-in" style="padding-top:80px">
            <h2>🔒 Login Required</h2>
            <p class="text-muted mt-12">Please login or create an account to access the Advisory system.</p>
            <div class="mt-24">
                <button class="btn btn-primary" onclick="navigate('login')">${t('login')}</button>
                <button class="btn btn-outline" onclick="navigate('register')" style="margin-left:8px">${t('signup')}</button>
            </div>
        </div>`;
    }
    return `
    <div class="page fade-in">
        <h2 class="section-title">${t('advisory_title')}</h2>
        <p class="section-subtitle">${t('advisory_sub')}</p>

        <div class="card card-elevated" id="inputForm">
            <form onsubmit="handlePrediction(event)">
                <!-- Location Selection -->
                <h3 style="margin-bottom:16px; display:flex; align-items:center; gap:8px;">📍 Location & Soil</h3>
                <div class="form-row-3">
                    <div class="form-group">
                        <label class="form-label">${t('select_state')} *</label>
                        <select id="stateSelect" class="form-select" required onchange="onStateChange(this.value)">
                            <option value="">-- ${t('select_state')} --</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label">${t('select_district')} *</label>
                        <select id="districtSelect" class="form-select" required>
                            <option value="">-- ${t('select_district')} --</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label">${t('select_soil')} *</label>
                        <select id="soilSelect" class="form-select" required>
                            <option value="">-- ${t('select_soil')} --</option>
                        </select>
                    </div>
                </div>
                <div class="form-row">
                    <div class="form-group">
                        <label class="form-label">${t('select_season')} *</label>
                        <select id="seasonSelect" class="form-select" required>
                            <option value="">-- ${t('select_season')} --</option>
                            <option value="Kharif">Kharif (Jun-Oct)</option>
                            <option value="Rabi">Rabi (Oct-Mar)</option>
                            <option value="Zaid">Zaid (Mar-Jun)</option>
                        </select>
                    </div>
                    <div class="form-group">
                        <label class="form-label">${t('area')} <span class="form-sublabel">(1 ha = 2.47 acres)</span></label>
                        <input type="number" id="areaInput" class="form-input" value="1" min="0.1" max="500" step="0.1">
                        <button type="button" class="help-toggle" onclick="toggleHelp('helpArea')">${t('what_is_this')}</button>
                        <div class="help-content" id="helpArea">${t('help_area') || 'Farm area in hectares.'}</div>
                    </div>
                </div>

                <!-- Soil Nutrients -->
                <h3 style="margin:24px 0 16px; display:flex; align-items:center; gap:8px;">🧪 Soil Nutrients</h3>
                <div class="form-row-3">
                    <div class="form-group">
                        <label class="form-label">${t('nitrogen')} <span class="form-sublabel">(kg/ha)</span></label>
                        <input type="number" id="nInput" class="form-input" placeholder="e.g. 80" min="0" max="500" step="1" required>
                        <button type="button" class="help-toggle" onclick="toggleHelp('helpN')">${t('what_is_this')}</button>
                        <div class="help-content" id="helpN">${t('help_n')}</div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">${t('phosphorus')} <span class="form-sublabel">(kg/ha)</span></label>
                        <input type="number" id="pInput" class="form-input" placeholder="e.g. 40" min="0" max="200" step="1" required>
                        <button type="button" class="help-toggle" onclick="toggleHelp('helpP')">${t('what_is_this')}</button>
                        <div class="help-content" id="helpP">${t('help_p')}</div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">${t('potassium')} <span class="form-sublabel">(kg/ha)</span></label>
                        <input type="number" id="kInput" class="form-input" placeholder="e.g. 40" min="0" max="500" step="1" required>
                        <button type="button" class="help-toggle" onclick="toggleHelp('helpK')">${t('what_is_this')}</button>
                        <div class="help-content" id="helpK">${t('help_k')}</div>
                    </div>
                </div>
                <div class="form-group">
                    <label class="form-label">${t('ph_level')} <span class="form-sublabel">(0–14)</span></label>
                    <input type="number" id="phInput" class="form-input" placeholder="e.g. 6.5" min="0" max="14" step="0.1" required>
                    <button type="button" class="help-toggle" onclick="toggleHelp('helpPH')">${t('what_is_this')}</button>
                    <div class="help-content" id="helpPH">${t('help_ph')}</div>
                </div>

                <!-- Climate -->
                <h3 style="margin:24px 0 16px; display:flex; align-items:center; gap:8px;">🌦️ Climate Conditions</h3>
                <div class="form-row-3">
                    <div class="form-group">
                        <label class="form-label">${t('temperature')}</label>
                        <input type="number" id="tempInput" class="form-input" placeholder="e.g. 28" min="-5" max="55" step="0.5" required>
                        <button type="button" class="help-toggle" onclick="toggleHelp('helpTemp')">${t('what_is_this')}</button>
                        <div class="help-content" id="helpTemp">${t('help_temp')}</div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">${t('humidity')}</label>
                        <input type="number" id="humidityInput" class="form-input" placeholder="e.g. 65" min="0" max="100" step="1" required>
                        <button type="button" class="help-toggle" onclick="toggleHelp('helpHumidity')">${t('what_is_this')}</button>
                        <div class="help-content" id="helpHumidity">${t('help_humidity')}</div>
                    </div>
                    <div class="form-group">
                        <label class="form-label">${t('rainfall')}</label>
                        <input type="number" id="rainfallInput" class="form-input" placeholder="e.g. 900" min="0" max="5000" step="10" required>
                        <button type="button" class="help-toggle" onclick="toggleHelp('helpRainfall')">${t('what_is_this')}</button>
                        <div class="help-content" id="helpRainfall">${t('help_rainfall')}</div>
                    </div>
                </div>

                <!-- Climate Simulation -->
                <div class="simulation-panel">
                    <h4>${t('climate_sim')}</h4>
                    <p style="font-size:0.82rem; color:var(--text-muted); margin-bottom:12px">${t('climate_sim_desc') || 'Adjust sliders to simulate climate change effects.'}</p>
                    <div class="form-row">
                        <div class="slider-group">
                            <div class="slider-header">
                                <span class="form-label">${t('rainfall_change') || 'Rainfall Change'}</span>
                                <span class="slider-value" id="rainChangeVal">0%</span>
                            </div>
                            <input type="range" id="rainChangeSlider" min="-50" max="50" value="0" oninput="document.getElementById('rainChangeVal').textContent=this.value+'%'">
                        </div>
                        <div class="slider-group">
                            <div class="slider-header">
                                <span class="form-label">${t('temp_change') || 'Temperature Change'}</span>
                                <span class="slider-value" id="tempChangeVal">0°C</span>
                            </div>
                            <input type="range" id="tempChangeSlider" min="-5" max="5" value="0" step="0.5" oninput="document.getElementById('tempChangeVal').textContent=this.value+'°C'">
                        </div>
                    </div>
                </div>

                <div style="margin-top:24px; text-align:center">
                    <button type="submit" class="btn btn-primary btn-lg" id="analyzeBtn">${t('analyze')}</button>
                </div>
            </form>
        </div>

        <!-- Results Area -->
        <div id="resultsArea"></div>
    </div>
    `;
}

async function initRecommendPage() {
    try {
        const data = await apiGetStates();
        const sel = document.getElementById('stateSelect');
        if (sel && data?.states) {
            data.states.forEach(s => {
                sel.innerHTML += `<option value="${s}">${s}</option>`;
            });
        }
    } catch (e) { }
}

async function onStateChange(state) {
    if (!state) return;
    try {
        // Load districts
        const dData = await apiGetDistricts(state);
        const dSel = document.getElementById('districtSelect');
        dSel.innerHTML = `<option value="">-- ${t('select_district')} --</option>`;
        if (dData?.districts) {
            dData.districts.forEach(d => dSel.innerHTML += `<option value="${d}">${d}</option>`);
        }

        // Load soil types
        const sData = await apiGetSoilTypes(state);
        const sSel = document.getElementById('soilSelect');
        sSel.innerHTML = `<option value="">-- ${t('select_soil')} --</option>`;
        if (sData?.soil_types) {
            sData.soil_types.forEach(s => sSel.innerHTML += `<option value="${s}">${s}</option>`);
        }

        // Load climate defaults
        const cData = await apiGetClimate(state);
        if (cData?.climate) {
            const c = cData.climate;
            const tempAvg = ((c.temp_min + c.temp_max) / 2).toFixed(1);
            const humAvg = ((c.humidity_min + c.humidity_max) / 2).toFixed(0);
            const rainAvg = ((c.rainfall_min + c.rainfall_max) / 2).toFixed(0);
            document.getElementById('tempInput').value = tempAvg;
            document.getElementById('humidityInput').value = humAvg;
            document.getElementById('rainfallInput').value = rainAvg;
        }
    } catch (e) { }
}

async function handlePrediction(e) {
    e.preventDefault();
    const rainChange = parseFloat(document.getElementById('rainChangeSlider').value) / 100;
    const tempChange = parseFloat(document.getElementById('tempChangeSlider').value);

    const baseRainfall = parseFloat(document.getElementById('rainfallInput').value);
    const baseTemp = parseFloat(document.getElementById('tempInput').value);

    const data = {
        n: parseFloat(document.getElementById('nInput').value),
        p: parseFloat(document.getElementById('pInput').value),
        k: parseFloat(document.getElementById('kInput').value),
        temperature: baseTemp + tempChange,
        humidity: parseFloat(document.getElementById('humidityInput').value),
        ph: parseFloat(document.getElementById('phInput').value),
        rainfall: baseRainfall * (1 + rainChange),
        soil_type: document.getElementById('soilSelect').value,
        state: document.getElementById('stateSelect').value,
        district: document.getElementById('districtSelect').value,
        season: document.getElementById('seasonSelect').value,
        area: parseFloat(document.getElementById('areaInput').value) || 1
    };

    formData = data;

    showLoading(t('loading'));
    try {
        const result = await apiFullPrediction(data);
        lastPredictionResult = result;
        hideLoading();
        renderResults(result, data);
    } catch (err) {
        hideLoading();
    }
}

function renderResults(result, input) {
    const crops = result.crop_recommendations?.recommendations || [];
    const yld = result.yield_prediction || {};
    const risk = result.risk_analysis || {};
    const importance = result.crop_recommendations?.feature_importance || {};

    const riskClass = (risk.risk_level || '').toLowerCase();
    const yieldDiff = yld.yield_difference_percent || 0;

    document.getElementById('resultsArea').innerHTML = `
    <div class="results-container fade-in" style="margin-top:32px">
        <!-- Crop Recommendations -->
        <div class="card result-card">
            <div class="result-header">
                <span class="result-icon">🌾</span>
                <h3>${t('crop_recommendations')}</h3>
            </div>
            ${crops.map((c, i) => `
                <div class="crop-rank rank-${i + 1}">
                    <span class="crop-rank-num">${i + 1}</span>
                    <span class="crop-rank-name">${c.crop}</span>
                    <span class="crop-rank-prob">${c.probability}%</span>
                </div>
            `).join('')}
            ${crops[0]?.explanation ? `
                <div class="explanation-box">
                    <strong>${t('explanation')}:</strong><br>${crops[0].explanation}
                </div>
            ` : ''}
        </div>

        <!-- Yield Prediction -->
        <div class="card result-card">
            <div class="result-header">
                <span class="result-icon">📊</span>
                <h3>${t('yield_prediction')}</h3>
            </div>
            <div class="yield-value">${yld.predicted_yield} <span class="yield-unit">${yld.unit || 'tons/ha'}</span></div>
            <div style="font-size:0.88rem; color:var(--text-muted); margin-top:4px">
                Total production: <strong>${yld.total_production} tons</strong> for ${input.area} ha
            </div>
            <div class="yield-comparison ${yieldDiff >= 0 ? 'yield-above' : 'yield-below'}" style="margin-top:12px">
                ${yieldDiff >= 0 ? '📈' : '📉'} ${Math.abs(yieldDiff)}% ${yieldDiff >= 0 ? 'above' : 'below'} state average (${yld.state_average_yield} tons/ha)
            </div>
        </div>

        <!-- Risk Analysis -->
        <div class="card result-card">
            <div class="result-header">
                <span class="result-icon">⚡</span>
                <h3>${t('risk_analysis')}</h3>
            </div>
            <div class="risk-badge risk-${riskClass}">
                ${riskClass === 'low' ? '✅' : riskClass === 'moderate' ? '⚠️' : '🔴'} ${risk.risk_level} Risk
                <span style="font-weight:400; font-size:0.82rem; margin-left:8px">(Score: ${risk.risk_score}/100)</span>
            </div>
            <div class="risk-factors">
                ${(risk.factors || []).map(f => `<div class="risk-factor">${f}</div>`).join('')}
            </div>
        </div>

        <!-- Feature Importance -->
        <div class="card result-card">
            <div class="result-header">
                <span class="result-icon">📉</span>
                <h3>${t('feature_importance')}</h3>
            </div>
            <div class="importance-bar-container">
                ${Object.entries(importance)
            .sort((a, b) => b[1] - a[1])
            .map(([name, val]) => `
                    <div class="importance-item">
                        <span class="importance-label">${name}</span>
                        <div class="importance-bar-bg"><div class="importance-bar" style="width:${val * 3}%"></div></div>
                        <span class="importance-value">${val}%</span>
                    </div>
                `).join('')}
            </div>
        </div>
    </div>
    `;
}

// ======================== DASHBOARD PAGE ========================
function renderDashboardPage() {
    if (!isLoggedIn()) {
        return `<div class="page page-narrow text-center fade-in" style="padding-top:80px">
            <h2>🔒 Login Required</h2>
            <p class="text-muted mt-12">Please login to view your dashboard.</p>
            <button class="btn btn-primary mt-24" onclick="navigate('login')">${t('login')}</button>
        </div>`;
    }
    return `
    <div class="page fade-in">
        <h2 class="section-title">${t('dashboard_title')}</h2>
        <p class="section-subtitle">${t('dashboard_sub') || 'Track your prediction history and compare yields.'}</p>

        <div class="dashboard-grid">
            <div class="card" style="grid-column: 1 / -1">
                <h3 style="margin-bottom:16px">${t('recent_predictions')}</h3>
                <div id="historyTable">${t('loading')}...</div>
            </div>
            <div class="card" id="yieldChartCard">
                <h3 style="margin-bottom:16px">${t('yield_comparison') || 'Yield Comparison'}</h3>
                <div id="yieldChart"></div>
            </div>
            <div class="card" id="statsCard">
                <h3 style="margin-bottom:16px">Prediction Summary</h3>
                <div id="predStats"></div>
            </div>
        </div>
    </div>
    `;
}

async function initDashboardPage() {
    try {
        const history = await apiGetHistory();
        const tbl = document.getElementById('historyTable');

        if (!history || history.length === 0) {
            tbl.innerHTML = `<p class="text-muted">${t('no_history')}</p>`;
            document.getElementById('yieldChart').innerHTML = '<p class="text-muted">No data yet.</p>';
            document.getElementById('predStats').innerHTML = '<p class="text-muted">No predictions made yet.</p>';
            return;
        }

        // Render table
        tbl.innerHTML = `
        <div style="overflow-x:auto">
        <table class="history-table">
            <thead><tr>
                <th>${t('date')}</th><th>${t('type')}</th><th>${t('state')}</th><th>${t('result')}</th>
            </tr></thead>
            <tbody>
                ${history.slice(0, 15).map(h => {
            const date = new Date(h.created_at).toLocaleDateString();
            let resultStr = '';
            if (h.prediction_type === 'full' && h.result_data?.crop_recommendations?.recommendations?.[0]) {
                resultStr = '🌾 ' + h.result_data.crop_recommendations.recommendations[0].crop;
            } else if (h.prediction_type === 'crop' && h.result_data?.recommendations?.[0]) {
                resultStr = '🌾 ' + h.result_data.recommendations[0].crop;
            } else if (h.prediction_type === 'yield') {
                resultStr = '📊 ' + (h.result_data?.predicted_yield || 'N/A') + ' t/ha';
            } else {
                resultStr = h.prediction_type;
            }
            return `<tr><td>${date}</td><td>${h.prediction_type}</td><td>${h.state || '-'}</td><td>${resultStr}</td></tr>`;
        }).join('')}
            </tbody>
        </table>
        </div>`;

        // Yield comparison chart
        const yieldEntries = history.filter(h =>
            h.prediction_type === 'full' && h.result_data?.yield_prediction
        ).slice(0, 6);

        if (yieldEntries.length > 0) {
            const maxYield = Math.max(...yieldEntries.map(e => Math.max(
                e.result_data.yield_prediction.predicted_yield || 0,
                e.result_data.yield_prediction.state_average_yield || 0
            )));

            document.getElementById('yieldChart').innerHTML = `
                <div class="bar-chart">
                    ${yieldEntries.map(e => {
                const pred = e.result_data.yield_prediction.predicted_yield;
                const avg = e.result_data.yield_prediction.state_average_yield;
                const crop = e.result_data.crop_recommendations?.recommendations?.[0]?.crop || 'Crop';
                const predH = (pred / maxYield * 160);
                const avgH = (avg / maxYield * 160);
                return `
                        <div class="bar-group">
                            <div style="display:flex; gap:4px; align-items:flex-end; height:180px">
                                <div class="bar bar-predicted" style="height:${predH}px; width:24px" title="${pred} t/ha"></div>
                                <div class="bar bar-average" style="height:${avgH}px; width:24px" title="${avg} t/ha"></div>
                            </div>
                            <div class="bar-label">${crop}</div>
                        </div>`;
            }).join('')}
                </div>
                <div class="chart-legend">
                    <span><span class="legend-dot" style="background:var(--primary)"></span> Predicted</span>
                    <span><span class="legend-dot" style="background:var(--accent-light); border:1px solid var(--accent)"></span> State Avg</span>
                </div>
            `;
        } else {
            document.getElementById('yieldChart').innerHTML = '<p class="text-muted">Run predictions to see yield comparisons.</p>';
        }

        // Stats
        const totalPreds = history.length;
        const cropPreds = history.filter(h => h.prediction_type === 'crop' || h.prediction_type === 'full').length;
        const states = [...new Set(history.map(h => h.state).filter(Boolean))];

        document.getElementById('predStats').innerHTML = `
            <div style="display:grid; gap:16px">
                <div style="text-align:center; padding:16px; background:var(--primary-lighter); border-radius:var(--radius-md)">
                    <div class="stat-number" style="font-size:1.8rem">${totalPreds}</div>
                    <div class="stat-label">Total Predictions</div>
                </div>
                <div style="text-align:center; padding:16px; background:var(--accent-light); border-radius:var(--radius-md)">
                    <div class="stat-number" style="font-size:1.8rem; color:var(--accent)">${cropPreds}</div>
                    <div class="stat-label">Crop Analyses</div>
                </div>
                <div style="text-align:center; padding:16px; background:#e3f2fd; border-radius:var(--radius-md)">
                    <div class="stat-number" style="font-size:1.8rem; color:#1976d2">${states.length}</div>
                    <div class="stat-label">States Analyzed</div>
                </div>
            </div>
        `;
    } catch (e) {
        document.getElementById('historyTable').innerHTML = '<p class="text-muted">Failed to load history.</p>';
    }
}

// ======================== CHATBOT PAGE ========================
let chatMessages = [];

function renderChatbotPage() {
    if (!isLoggedIn()) {
        return `<div class="page page-narrow text-center fade-in" style="padding-top:80px">
            <h2>🔒 Login Required</h2>
            <p class="text-muted mt-12">Please login to use the AI chatbot.</p>
            <button class="btn btn-primary mt-24" onclick="navigate('login')">${t('login')}</button>
        </div>`;
    }
    return `
    <div class="page page-narrow fade-in">
        <h2 class="section-title">${t('chat_title')}</h2>
        <p class="section-subtitle" style="margin-bottom:16px">${t('chat_sub') || 'Ask me anything about farming.'}</p>

        <div class="quick-actions">
            <button class="quick-btn" onclick="sendQuickChat('What is NPK?')">What is NPK?</button>
            <button class="quick-btn" onclick="sendQuickChat('How to improve soil?')">Improve Soil</button>
            <button class="quick-btn" onclick="sendQuickChat('Government schemes')">Gov Schemes</button>
            <button class="quick-btn" onclick="sendQuickChat('Tell me about Rice')">About Rice</button>
            <button class="quick-btn" onclick="sendQuickChat('Tell me about Maharashtra')">Maharashtra</button>
            <button class="quick-btn" onclick="sendQuickChat('Soil Health Card')">Soil Health Card</button>
        </div>

        <div class="card" style="padding:0; overflow:hidden; height: calc(100vh - 340px); display:flex; flex-direction:column">
            <div class="chat-messages" id="chatMessages">
                <div class="chat-msg bot">
                    <div class="chat-avatar">🌾</div>
                    <div class="chat-bubble">🙏 Namaste! I am BharatAgri AI Assistant.\n\nI can help you with:\n• 🌱 Crop information\n• 🧪 Soil guidance (NPK, pH)\n• 📊 Recommendation explanations\n• 🏛️ Government schemes\n• 🗺️ State agricultural data\n\nJust ask me anything about farming!</div>
                </div>
            </div>
            <div class="chat-input-area" style="padding:12px 16px; border-top:1px solid var(--border-light)">
                <input type="text" id="chatInput" class="chat-input" placeholder="${t('chat_placeholder')}" onkeydown="if(event.key==='Enter')sendChat()">
                <button class="btn btn-primary" onclick="sendChat()">${t('send')}</button>
            </div>
        </div>
    </div>
    `;
}

async function sendChat() {
    const input = document.getElementById('chatInput');
    const msg = input.value.trim();
    if (!msg) return;
    input.value = '';

    // Add user message
    appendChatMsg(msg, 'user');

    try {
        const data = await apiChatMessage(msg, currentLang, formData);
        if (data?.response) {
            appendChatMsg(data.response, 'bot');
        }
    } catch (e) {
        appendChatMsg('Sorry, I couldn\'t process your request. Please try again.', 'bot');
    }
}

function sendQuickChat(msg) {
    document.getElementById('chatInput').value = msg;
    sendChat();
}

function appendChatMsg(text, type) {
    const container = document.getElementById('chatMessages');
    const avatar = type === 'user' ? '👤' : '🌾';
    // Simple markdown-like bold processing
    let processedText = text.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    container.innerHTML += `
        <div class="chat-msg ${type}">
            <div class="chat-avatar">${avatar}</div>
            <div class="chat-bubble">${processedText}</div>
        </div>
    `;
    container.scrollTop = container.scrollHeight;
}

// ======================== PROFILE PAGE ========================
function renderProfilePage() {
    if (!isLoggedIn()) {
        navigate('login');
        return '';
    }
    const user = getUser();
    return `
    <div class="page page-narrow fade-in">
        <h2 class="section-title">${t('profile_title')}</h2>
        <div class="card" style="margin-top:24px">
            <div class="profile-header">
                <div class="profile-avatar">👤</div>
                <div>
                    <h3>${user?.name || 'User'}</h3>
                    <p class="text-muted" style="font-size:0.88rem">${user?.email || ''}</p>
                </div>
            </div>
            <div class="form-group">
                <label class="form-label">${t('name')}</label>
                <input type="text" id="profileName" class="form-input" value="${user?.name || ''}">
            </div>
            <div class="form-group">
                <label class="form-label">${t('email')}</label>
                <input type="email" class="form-input" value="${user?.email || ''}" disabled style="opacity:0.6">
            </div>
            <div class="form-group">
                <label class="form-label">${t('state') || 'State'}</label>
                <input type="text" id="profileState" class="form-input" value="${user?.state || ''}">
            </div>
            <div class="form-group">
                <label class="form-label">${t('preferred_language') || 'Preferred Language'}</label>
                <select id="profileLang" class="form-select">
                    <option value="en" ${user?.language === 'en' ? 'selected' : ''}>English</option>
                    <option value="hi" ${user?.language === 'hi' ? 'selected' : ''}>हिन्दी</option>
                    <option value="pa" ${user?.language === 'pa' ? 'selected' : ''}>ਪੰਜਾਬੀ</option>
                    <option value="mr" ${user?.language === 'mr' ? 'selected' : ''}>मराठी</option>
                    <option value="te" ${user?.language === 'te' ? 'selected' : ''}>తెలుగు</option>
                    <option value="ta" ${user?.language === 'ta' ? 'selected' : ''}>தமிழ்</option>
                    <option value="bn" ${user?.language === 'bn' ? 'selected' : ''}>বাংলা</option>
                    <option value="gu" ${user?.language === 'gu' ? 'selected' : ''}>ગુજરાતી</option>
                </select>
            </div>
            <button class="btn btn-primary" onclick="saveProfile()">${t('save_changes')}</button>
        </div>
    </div>
    `;
}

async function saveProfile() {
    // Profile save is a nice-to-have; for now just update local state
    const user = getUser();
    user.name = document.getElementById('profileName').value;
    user.state = document.getElementById('profileState').value;
    user.language = document.getElementById('profileLang').value;
    localStorage.setItem('bharatagri_user', JSON.stringify(user));
    changeLanguage(user.language);
    updateAuthUI();
    showToast('Profile updated successfully!');
}

// ======================== HELPERS ========================
function toggleHelp(id) {
    const el = document.getElementById(id);
    el.classList.toggle('show');
}

function toggleMobileMenu() {
    document.getElementById('navLinks').classList.toggle('show');
}

// ======================== ADMIN PAGE ========================
function renderAdminPage() {
    return `
    <div class="page fade-in">
        <h2 class="section-title">🛡️ Admin Dashboard</h2>
        <p class="section-subtitle">Developer view — user signups, predictions, and chat activity.</p>

        <div class="card" style="margin-bottom:24px" id="adminKeyCard">
            <h3 style="margin-bottom:12px">🔑 Admin Authentication</h3>
            <div class="form-row" style="align-items:flex-end">
                <div class="form-group" style="flex:1">
                    <label class="form-label">Admin Secret Key</label>
                    <input type="password" id="adminKeyInput" class="form-input" placeholder="Enter admin secret key...">
                </div>
                <div class="form-group" style="flex:0">
                    <button class="btn btn-primary" onclick="authenticateAdmin()">Unlock</button>
                </div>
            </div>
        </div>

        <div id="adminContent" style="display:none">
            <!-- Stats Cards -->
            <div class="stats-strip fade-in" style="margin-bottom:24px" id="adminStats">
                <div class="stat-item">
                    <div class="stat-number" id="statUsers">-</div>
                    <div class="stat-label">Total Users</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" id="statPredictions">-</div>
                    <div class="stat-label">Total Predictions</div>
                </div>
                <div class="stat-item">
                    <div class="stat-number" id="statChats">-</div>
                    <div class="stat-label">Chat Messages</div>
                </div>
            </div>

            <!-- Users Table -->
            <div class="card" style="margin-bottom:24px">
                <h3 style="margin-bottom:16px">👥 Registered Users</h3>
                <div style="overflow-x:auto" id="adminUsersTable">Loading...</div>
            </div>

            <!-- Predictions Table -->
            <div class="card" style="margin-bottom:24px">
                <h3 style="margin-bottom:16px">📊 All Predictions</h3>
                <div style="overflow-x:auto" id="adminPredTable">Loading...</div>
            </div>

            <!-- Chats Table -->
            <div class="card" style="margin-bottom:24px">
                <h3 style="margin-bottom:16px">💬 Chat History</h3>
                <div style="overflow-x:auto" id="adminChatsTable">Loading...</div>
            </div>
        </div>
    </div>
    `;
}

function initAdminPage() {
    // Auto-unlock if key already stored
    const savedKey = sessionStorage.getItem('bharatagri_admin_key');
    if (savedKey) {
        document.getElementById('adminKeyInput').value = savedKey;
        authenticateAdmin();
    }
}

async function authenticateAdmin() {
    const key = document.getElementById('adminKeyInput').value.trim();
    if (!key) { showToast('Please enter the admin key', 'error'); return; }
    sessionStorage.setItem('bharatagri_admin_key', key);

    try {
        const stats = await apiAdminStats();
        // Success — show admin content
        document.getElementById('adminKeyCard').style.display = 'none';
        document.getElementById('adminContent').style.display = 'block';

        // Populate stats
        document.getElementById('statUsers').textContent = stats.total_users;
        document.getElementById('statPredictions').textContent = stats.total_predictions;
        document.getElementById('statChats').textContent = stats.total_chats;

        // Load all data
        loadAdminUsers();
        loadAdminPredictions();
        loadAdminChats();
    } catch (e) {
        sessionStorage.removeItem('bharatagri_admin_key');
        showToast('Invalid admin key', 'error');
    }
}

async function loadAdminUsers() {
    try {
        const users = await apiAdminUsers();
        const el = document.getElementById('adminUsersTable');
        if (!users.length) { el.innerHTML = '<p class="text-muted">No users yet.</p>'; return; }
        el.innerHTML = `
        <table class="history-table">
            <thead><tr>
                <th>#</th><th>Name</th><th>Email</th><th>State</th><th>Lang</th><th>Predictions</th><th>Joined</th>
            </tr></thead>
            <tbody>
                ${users.map((u, i) => `<tr>
                    <td>${i + 1}</td>
                    <td><strong>${u.name}</strong></td>
                    <td>${u.email}</td>
                    <td>${u.state || '-'}</td>
                    <td>${u.language || 'en'}</td>
                    <td>${u.prediction_count}</td>
                    <td>${u.created_at ? new Date(u.created_at).toLocaleDateString() : '-'}</td>
                </tr>`).join('')}
            </tbody>
        </table>`;
    } catch (e) {
        document.getElementById('adminUsersTable').innerHTML = '<p class="text-muted">Failed to load users.</p>';
    }
}

async function loadAdminPredictions() {
    try {
        const preds = await apiAdminPredictions();
        const el = document.getElementById('adminPredTable');
        if (!preds.length) { el.innerHTML = '<p class="text-muted">No predictions yet.</p>'; return; }
        el.innerHTML = `
        <table class="history-table">
            <thead><tr>
                <th>User</th><th>Type</th><th>State</th><th>Top Crop / Result</th><th>Date</th>
            </tr></thead>
            <tbody>
                ${preds.slice(0, 100).map(p => {
            let result = '-';
            if (p.prediction_type === 'full' && p.result_data?.crop_recommendations?.recommendations?.[0]) {
                const r = p.result_data.crop_recommendations.recommendations;
                result = r.map(c => c.crop + ' (' + c.probability + '%)').join(', ');
            } else if (p.prediction_type === 'crop' && p.result_data?.recommendations?.[0]) {
                result = p.result_data.recommendations[0].crop;
            } else if (p.prediction_type === 'yield' && p.result_data?.predicted_yield) {
                result = p.result_data.predicted_yield + ' t/ha';
            } else if (p.prediction_type === 'risk') {
                result = (p.result_data?.risk_level || '-') + ' (' + (p.result_data?.risk_score || 0) + '/100)';
            }
            return `<tr>
                        <td><strong>${p.user_name}</strong><br><span style="font-size:0.75rem;color:var(--text-muted)">${p.user_email}</span></td>
                        <td>${p.prediction_type}</td>
                        <td>${p.state || '-'}</td>
                        <td style="max-width:300px">${result}</td>
                        <td>${p.created_at ? new Date(p.created_at).toLocaleString() : '-'}</td>
                    </tr>`;
        }).join('')}
            </tbody>
        </table>`;
    } catch (e) {
        document.getElementById('adminPredTable').innerHTML = '<p class="text-muted">Failed to load predictions.</p>';
    }
}

async function loadAdminChats() {
    try {
        const chats = await apiAdminChats();
        const el = document.getElementById('adminChatsTable');
        if (!chats.length) { el.innerHTML = '<p class="text-muted">No chats yet.</p>'; return; }
        el.innerHTML = `
        <table class="history-table">
            <thead><tr>
                <th>User</th><th>Message</th><th>Response</th><th>Lang</th><th>Date</th>
            </tr></thead>
            <tbody>
                ${chats.slice(0, 100).map(c => `<tr>
                    <td><strong>${c.user_name}</strong></td>
                    <td style="max-width:200px">${c.message}</td>
                    <td style="max-width:300px; font-size:0.82rem">${(c.response || '').substring(0, 120)}${(c.response || '').length > 120 ? '...' : ''}</td>
                    <td>${c.language}</td>
                    <td>${c.created_at ? new Date(c.created_at).toLocaleString() : '-'}</td>
                </tr>`).join('')}
            </tbody>
        </table>`;
    } catch (e) {
        document.getElementById('adminChatsTable').innerHTML = '<p class="text-muted">Failed to load chats.</p>';
    }
}

