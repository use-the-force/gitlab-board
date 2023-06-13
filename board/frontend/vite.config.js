import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import 'dotenv/config'

// https://vitejs.dev/config/

export default defineConfig(({ command, mode }) => {
    return {
        plugins: [svelte()],
        base: process.env.BOARD_SUBPATH,
        define: {
            global: {
                BOARD_SUBPATH: process.env.BOARD_SUBPATH,
                VITE_BOARD_API_URL: process.env.VITE_BOARD_API_URL,
                VITE_GITLAB_API_TOKEN: process.env.VITE_GITLAB_API_TOKEN,
                VITE_GITLAB_API_URL: process.env.VITE_GITLAB_API_URL,
                VITE_LOGO_URL: process.env.VITE_LOGO_URL,
            }
        },
    };
});
