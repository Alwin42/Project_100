import { defineStore } from 'pinia';
import api from '../services/api';

export const useTaskStore = defineStore('task', {
  state: () => ({
    tasks: [],
    loading: false,
    error: null
  }),

  actions: {
    // 1. Fetch all tasks from Backend
    async fetchTasks() {
      this.loading = true;
      try {
        const response = await api.get('tasks/');
        this.tasks = response.data;
      } catch (err) {
        this.error = "Failed to load tasks";
        console.error(err);
      } finally {
        this.loading = false;
      }
    },

    // 2. Add a new task
    async addTask(title, priority) {
      try {
        const response = await api.post('tasks/', {
          title: title,
          priority: priority,
          is_done: false
        });
        // Add the new task directly to the list (so we don't have to refresh)
        this.tasks.unshift(response.data); 
      } catch (err) {
        console.error("Failed to add task", err);
      }
    },

    // 3. Toggle Task Completion
    async toggleTask(id, isDone) {
      try {
        // Optimistic update (update UI immediately)
        const task = this.tasks.find(t => t.id === id);
        if (task) task.is_done = isDone;

        await api.patch(`tasks/${id}/`, { is_done: isDone });
      } catch (err) {
        console.error("Failed to update task", err);
      }
    }
  }
});