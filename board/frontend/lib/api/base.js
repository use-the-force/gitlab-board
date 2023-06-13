const BOARD_API_URL = global.VITE_BOARD_API_URL;

export const fetchapi = async (resource, options) => {
    await fetch(`${BOARD_API_URL}/auth/csrftoken`, {
        credentials: "include"
    });

    const res = await fetch(resource, options);

    if (res.status === 401) {
        window.location.href = `${BOARD_API_URL}/login`;
    } else {
        return res;
    }
};
