import Cookies from "js-cookie";

import { setAuthorized } from "../store";

const loginPath = `/${global.BOARD_SUBPATH}login`;

export const isAuthorized = () => {
    return Cookies.get("authorized") ?? false;
};

export const authRequired = () => {
    if (!isAuthorized() && window.location.pathname !== loginPath) {
        window.location.href = loginPath;
    }
};

export const logout = () => {
    Cookies.remove("authorized");
    Cookies.remove("token");

    window.location.href = loginPath;
    setAuthorized(false);
};
