import Cookies from "js-cookie";

import { setAuthorized } from "../store";

export const isAuthorized = () => {
    return Cookies.get("authorized") ?? false;
};

export const authRequired = () => {
    if (!isAuthorized() && window.location.pathname !== "/login") {
        window.location.href = "/login";
    }
};

export const logout = () => {
    Cookies.remove("authorized");
    Cookies.remove("token");

    window.location.href = "/login";
    setAuthorized(false);
};
