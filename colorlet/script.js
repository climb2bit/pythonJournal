// -------- BLOOKS DATA --------
const blooks = [
  // COMMON (35% total)
  { name: '⚪️ White Blob', rarity: 'common', chance: 11.67 },
  { name: '⚫️ Black Blob', rarity: 'common', chance: 11.67 },
  { name: '🤎 Brown Blob', rarity: 'common', chance: 11.66 },

  // UNCOMMON (30%)
  { name: '🔵 Blue Blob', rarity: 'uncommon', chance: 10 },
  { name: '🟢 Green Blob', rarity: 'uncommon', chance: 10 },
  { name: '💖 Pink Blob', rarity: 'uncommon', chance: 10 },

  // RARE (20%)
  { name: '🔴 Red Blob', rarity: 'rare', chance: 10 },
  { name: '🟠 Orange Blob', rarity: 'rare', chance: 10 },

  // EPIC (14.35%)
  { name: '🟣 Purple Blob', rarity: 'epic', chance: 7.18 },
  { name: '🟡 Yellow Blob', rarity: 'epic', chance: 7.17 },

  // LEGENDARY (0.5%)
  { name: '🌈 Rainbow Blob', rarity: 'legendary', chance: 0.5 },

  // CHROMA (0.15%)
  { name: '✨ Gold Blob', rarity: 'chroma', chance: 0.05 },
  { name: '🪙 Silver Blob', rarity: 'chroma', chance: 0.05 },
  { name: '🟤 Bronze Blob', rarity: 'chroma', chance: 0.05 }
];

function buildPackRatesTooltip() {
  const tooltip = document.getElementById('packRatesTooltip');
  tooltip.innerHTML = '<strong>🎁 Pack Drop Rates</strong><br>';

  for (const blook of blooks) {
    const line = document.createElement('div');
    line.textContent = `${blook.name}`;
    line.title = `${blook.name} — ${blook.chance}% chance`;
    line.style.cursor = 'default'; // show pointer for clarity
    tooltip.appendChild(line);
  }
}

// Build the tooltip on page load
window.onload = () => {
  if (currentUser && users[currentUser]) {
    loadUserData();
  } else {
    showLogin();
  }
  buildPackRatesTooltip();
};


// -------- VARIABLES --------
let users = JSON.parse(localStorage.getItem('users') || '{}');
let currentUser = localStorage.getItem('currentUser');
let tokens = 0;
let inventory = {};
let lastDailyClaim = null;

// -------- AUTH CHECK --------
function requireLogin() {
  if (!currentUser || !users[currentUser]) {
    window.location.href = 'index.html';
  }
}

// -------- INIT PAGE DATA --------
function loadUserData() {
  if (!currentUser || !users[currentUser]) return;

  const user = users[currentUser];
  tokens = user.tokens || 0;
  inventory = user.inventory || {};
  lastDailyClaim = user.lastDailyClaim || null;

  const displayUser = document.getElementById('currentUserDisplay');
  const displayTokens = document.getElementById('tokenCount');

  if (displayUser) displayUser.innerText = currentUser;
  if (displayTokens) displayTokens.innerText = tokens;

  const inventoryList = document.getElementById('inventoryList');
  if (inventoryList) updateInventoryDisplay();
}

function saveUsers() {
  localStorage.setItem('users', JSON.stringify(users));
}

function saveUserData() {
  if (!currentUser) return;
  users[currentUser].tokens = tokens;
  users[currentUser].inventory = inventory;
  users[currentUser].lastDailyClaim = lastDailyClaim;
  saveUsers();
}

// -------- LOGIN / REGISTER --------
function login() {
  const input = document.getElementById('usernameInput').value.trim();
  const msg = document.getElementById('loginMessage');
  if (!input) {
    msg.textContent = 'Please enter your username.';
    return;
  }
  if (!users[input]) {
    msg.textContent = 'User not found. Please register first.';
    return;
  }
  currentUser = input;
  localStorage.setItem('currentUser', currentUser);
  window.location.href = 'market.html';
}

function register() {
  const input = document.getElementById('usernameInput').value.trim();
  const msg = document.getElementById('loginMessage');
  if (!input) {
    msg.textContent = 'Please enter a username.';
    return;
  }
  if (users[input]) {
    msg.textContent = 'Username already taken.';
    return;
  }

  users[input] = {
    tokens: 100,
    inventory: {},
    lastDailyClaim: null,
  };

  currentUser = input;
  localStorage.setItem('currentUser', currentUser);
  saveUsers();
  window.location.href = 'market.html';
}

// -------- LOGOUT / DELETE ACCOUNT --------
function logout() {
  currentUser = null;
  localStorage.removeItem('currentUser');
  window.location.href = 'index.html';
}

function deleteAccount() {
  if (!currentUser) return;
  const confirmDelete = confirm(`Delete account "${currentUser}" permanently?`);
  if (!confirmDelete) return;

  delete users[currentUser];
  saveUsers();
  currentUser = null;
  localStorage.removeItem('currentUser');
  alert('Account deleted.');
  window.location.href = 'index.html';
}

// -------- USERNAME CHANGE --------
function changeUsername() {
  const newUsername = document.getElementById('newUsernameInput').value.trim();
  const msg = document.getElementById('changeUsernameMessage');
  msg.textContent = '';

  if (!newUsername) {
    msg.textContent = 'Please enter a new username.';
    return;
  }
  if (users[newUsername]) {
    msg.textContent = 'Username already taken.';
    return;
  }

  users[newUsername] = users[currentUser];
  delete users[currentUser];
  currentUser = newUsername;
  localStorage.setItem('currentUser', currentUser);
  saveUsers();
  document.getElementById('currentUserDisplay').innerText = currentUser;
  msg.style.color = 'green';
  msg.textContent = 'Username changed successfully!';
  document.getElementById('newUsernameInput').value = '';
}

// -------- OPEN PACK --------
function openColorPack() {
  if (tokens < 25) {
    alert('Not enough tokens!');
    return;
  }

  tokens -= 25;

  let roll = Math.random() * 100;
  let total = 0;
  let selected = null;

  for (let blook of blooks) {
    total += blook.chance;
    if (roll <= total) {
      selected = blook;
      break;
    }
  }

  if (!selected) {
    alert('No blob found. Try again.');
    return;
  }

  inventory[selected.name] = (inventory[selected.name] || 0) + 1;
  saveUserData();

  const tokenSpan = document.getElementById('tokenCount');
  if (tokenSpan) tokenSpan.innerText = tokens;

  const resultDiv = document.getElementById('result');
  if (resultDiv) {
    resultDiv.className = `result ${selected.rarity}`;
    resultDiv.innerHTML = `You got: <strong>${selected.name}</strong><br><em>Rarity: ${selected.rarity.toUpperCase()}</em>`;
    resultDiv.style.display = 'inline-block';
  }

  updateInventoryDisplay();
}

// -------- DAILY REWARD --------
function claimDaily() {
  const now = Date.now();
  if (lastDailyClaim && now - lastDailyClaim < 24 * 60 * 60 * 1000) {
    alert('Daily reward already claimed!');
    return;
  }

  const rewards = [100, 200, 300, 400, 500, 1000];
  const reward = rewards[Math.floor(Math.random() * rewards.length)];
  tokens += reward;
  lastDailyClaim = now;

  alert(`You received ${reward} tokens!`);
  saveUserData();

  const tokenSpan = document.getElementById('tokenCount');
  if (tokenSpan) tokenSpan.innerText = tokens;
}

// -------- SELL DUPLICATES --------
function sellDuplicates() {
  let earned = 0;
  for (const name in inventory) {
    if (inventory[name] > 1) {
      const duplicates = inventory[name] - 1;
      const rarity = blooks.find(b => b.name === name)?.rarity || 'common';
      let value = 0;
      switch (rarity) {
        case 'common': value = 5; break;
        case 'uncommon': value = 10; break;
        case 'rare': value = 20; break;
        case 'epic': value = 40; break;
        case 'legendary': value = 100; break;
        case 'chroma': value = 200; break;
      }
      earned += value * duplicates;
      inventory[name] = 1;
    }
  }

  if (earned > 0) {
    tokens += earned;
    alert(`Sold duplicates for ${earned} tokens!`);
  } else {
    alert('No duplicates to sell.');
  }

  saveUserData();

  const tokenSpan = document.getElementById('tokenCount');
  if (tokenSpan) tokenSpan.innerText = tokens;

  updateInventoryDisplay();
}

// -------- DISPLAY INVENTORY --------
function updateInventoryDisplay() {
  const list = document.getElementById('inventoryList');
  if (!list) return;

  list.innerHTML = '';
  const names = Object.keys(inventory);

  if (names.length === 0) {
    list.innerHTML = '<li>No blobs yet!</li>';
    return;
  }

  names.sort((a, b) => {
    const getRarityIndex = (name) =>
      ['common', 'uncommon', 'rare', 'epic', 'legendary', 'chroma']
        .indexOf(blooks.find(b => b.name === name)?.rarity || 'common');
    return getRarityIndex(a) - getRarityIndex(b);
  });

  for (const name of names) {
    const rarity = blooks.find(b => b.name === name)?.rarity || 'common';
    const li = document.createElement('li');
    li.className = rarity;
    li.textContent = `${name} ×${inventory[name]}`;
    list.appendChild(li);
  }
}

// -------- PAGE LOAD --------
window.onload = () => {
  if (document.body.contains(document.getElementById('usernameInput'))) {
    // Login/register page – no need to load user data
    return;
  }

  requireLogin();
  loadUserData();
};
