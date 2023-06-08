import { defineConfig } from "vite";
import { svelte } from "@sveltejs/vite-plugin-svelte";
import 'dotenv/config'

// https://vitejs.dev/config/

export default defineConfig(({ command, mode }) => {
    return {
        plugins: [svelte()],
        define: {
            global: {
                BOARD_SUBPATH: process.env.BOARD_SUBPATH
            }
        },
    };
});
