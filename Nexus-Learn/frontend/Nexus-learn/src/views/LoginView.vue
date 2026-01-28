<template>
  <div class="login-container">
    <div class="login-card">
      <h2>Student Login</h2>
      <form @submit.prevent="handleLogin">
        
        <div class="form-group">
          <label>Username</label>
          <input 
            v-model="username" 
            type="text" 
            placeholder="Enter your Reg No or Username" 
            required
          />
        </div>

        <div class="form-group">
          <label>Password</label>
          <input 
            v-model="password" 
            type="password" 
            placeholder="Enter password" 
            required
          />
        </div>

        <p v-if="errorMessage" class="error">{{ errorMessage }}</p>

        <button type="submit" :disabled="isLoading">
          {{ isLoading ? 'Logging in...' : 'Login' }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useAuthStore } from '../stores/auth';

const authStore = useAuthStore();
const username = ref('');
const password = ref('');
const errorMessage = ref('');
const isLoading = ref(false);

const handleLogin = async () => {
  isLoading.value = true;
  errorMessage.value = '';
  
  try {
    await authStore.login(username.value, password.value);
  } catch (error) {
    errorMessage.value = 'Invalid username or password';
  } finally {
    isLoading.value = false;
  }
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 80vh;
  background-color: #f4f4f9;
}

.login-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
}

.form-group {
  margin-bottom: 1rem;
}

input {
  width: 100%;
  padding: 0.8rem;
  margin-top: 0.5rem;
  border: 1px solid #ddd;
  border-radius: 6px;
}

button {
  width: 100%;
  padding: 0.8rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  font-weight: bold;
}

button:disabled {
  background-color: #a5d6a7;
}

.error {
  color: red;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}
</style>
