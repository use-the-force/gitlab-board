import Cookies from "js-cookie";
import { fetchapi } from "./base";

const BOARD_API_URL = global.VITE_BOARD_API_URL;

export const login = async (username, password) => {
    const res = await fetchapi(`${BOARD_API_URL}/auth/login`, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        },
        body: JSON.stringify({
            username,
            password
        })
    });

    // TODO: implement proper UI validation
    if (res.status >= 400) {
        alert("User does not exists");
    }
};

export const getTeams = async () => {
    return await fetchapi(`${BOARD_API_URL}/teams/`, {
        method: "GET",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        }
    });
};

export const addTeam = async (name) => {
    return await fetchapi(`${BOARD_API_URL}/teams/`, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        },
        body: JSON.stringify({ name })
    });
};

export const deleteTeam = async (id) => {
    return await fetchapi(`${BOARD_API_URL}/teams/${id}`, {
        method: "DELETE",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        }
    });
};

export const getTeamProjects = async (teamId) => {
    return await fetchapi(`${BOARD_API_URL}/teams/${teamId}/projects`, {
        method: "GET",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        }
    });
};

export const attachTeamProject = async (teamId, projectId) => {
    return await fetchapi(`${BOARD_API_URL}/teams/${teamId}/projects`, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        },
        body: JSON.stringify({ gitlab_project_id: projectId })
    });
};

export const detachTeamProject = async (teamId, projectId) => {
    return await fetchapi(`${BOARD_API_URL}/teams/${teamId}/projects/${projectId}`, {
        method: "DELETE",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        }
    });
};

export const addTeamColumn = async (teamId, name, color) => {
    return await fetchapi(`${BOARD_API_URL}/teams/${teamId}/columns`, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        },
        body: JSON.stringify({ name, color })
    });
};

export const deleteTeamColumn = async (teamId, columnId) => {
    return await fetchapi(`${BOARD_API_URL}/teams/${teamId}/columns/${columnId}`, {
        method: "DELETE",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        }
    });
};

export const attachTeamColumnStatus = async (teamId, columnId, statusId) => {
    return await fetchapi(`${BOARD_API_URL}/teams/${teamId}/columns/${columnId}/labels`, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        },
        body: JSON.stringify({ gitlab_label_id: statusId })
    });
};

export const detachTeamColumnStatus = async (teamId, columnId, statusId) => {
    return await fetchapi(`${BOARD_API_URL}/teams/${teamId}/columns/${columnId}/labels/${statusId}`, {
        method: "DELETE",
        credentials: "include",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": Cookies.get("csrftoken")
        }
    });
};
