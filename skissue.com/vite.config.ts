import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";

export default defineConfig({
  plugins: [vue()],
  build: {
    rollupOptions: {
      input: {
        index: "public/index.html", // Login page
        info: "public/info.html",   // Home page
        userFiles: "public/userFiles.html"
      }
    }
  },
  server: {
    open: "public/index.html" // Ensure Vite opens the login page first
  }
});
