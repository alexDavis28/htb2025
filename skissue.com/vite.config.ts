import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      input: {
        index: "public/index.html", // Login page
        home: "public/home.html",   // Home page
      }
    }
  },
  server: {
    open: "public/index.html" // Ensure Vite opens the login page first
  }
});
