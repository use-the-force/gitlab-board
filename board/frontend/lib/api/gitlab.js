const GITLAB_API_URL = import.meta.env.VITE_GITLAB_API_URL;
const GITLAB_API_TOKEN = import.meta.env.VITE_GITLAB_API_TOKEN;

export const getProjects = async () => {
    const perPage = 100;
    const projects = [];
    let page = 1;
    let data = null;

    do {
        try {
            const res = await fetch(`${GITLAB_API_URL}/projects?per_page=${perPage}&page=${page}`,
                {
                    headers: {
                        "PRIVATE-TOKEN": GITLAB_API_TOKEN
                    }
                });
            data = await res.json();
            projects.push(...data);
        } catch {
        }
        ++page;
    } while (data.length === perPage || !data);

    return projects.sort((a, b) => a.name_with_namespace.localeCompare(b.name_with_namespace));
};

export const getAllProjectsMembers = async (projectIds) => {
    const calls = [];

    for (const id of projectIds) {
        calls.push(getProjectMembers(id));
    }

    const members = [].concat.apply([], await Promise.all(calls));

    console.log(">>> members", members);
    const uniqMembers = [...new Map(members.map((i) => [i.id, i])).values()];
    const filteredMembers = uniqMembers.filter(i => i.state === "active");
    console.log(">>> filteredMembers", filteredMembers);
    return filteredMembers;
};

export const getProjectMembers = async (projectId) => {
    const perPage = 100;
    const members = [];
    let page = 1;
    let data = null;

    do {
        try {
            const res = await fetch(`${GITLAB_API_URL}/projects/${projectId}/members/all?per_page=${perPage}&page=${page}`,
                {
                    headers: {
                        "PRIVATE-TOKEN": GITLAB_API_TOKEN
                    }
                });
            data = await res.json();
            members.push(...data);
        } catch {
        }
        ++page;
    } while (data.length === perPage || !data);

    return members;
};

export const getAllProjectsIssues = async (projectIds) => {
    const calls = [];

    for (const id of projectIds) {
        calls.push(getProjectIssues(id));
    }

    return [].concat.apply([], await Promise.all(calls));
};

export const getProjectIssues = async (projectId) => {
    const perPage = 100;
    const issues = [];
    let page = 1;
    let data = null;

    do {
        try {
            const res = await fetch(`${GITLAB_API_URL}/projects/${projectId}/issues?state=opened&per_page=${perPage}&page=${page}`,
                {
                    headers: {
                        "PRIVATE-TOKEN": GITLAB_API_TOKEN
                    }
                });
            data = await res.json();
            for (let i of data) {
                const mrs = await getProjectIssueMRs(projectId, i.iid);
                i.merge_requests = mrs;
            }
            issues.push(...data);
        } catch {
        }

        ++page;
    } while (data.length === perPage || !data);

    return issues;
};

export const getAllProjectsLabels = async (projectIds) => {
    const calls = [];

    for (const id of projectIds) {
        calls.push(getProjectLabels(id));
    }

    return [].concat.apply([], await Promise.all(calls));
};

export const getProjectLabels = async (projectId) => {
    const perPage = 100;
    const labels = [];
    let page = 1;
    let data = null;

    do {
        try {
            const res = await fetch(`${GITLAB_API_URL}/projects/${projectId}/labels?per_page=${perPage}&page=${page}`,
                {
                    headers: {
                        "PRIVATE-TOKEN": GITLAB_API_TOKEN
                    }
                });
            data = await res.json();
            labels.push(...data);
        } catch {
        }

        ++page;
    } while (data.length === perPage || !data);

    return labels;
};

export const getProjectIssueMRs = async (projectId, issueId) => {

    const res = await fetch(
        `${GITLAB_API_URL}/projects/${projectId}/issues/${issueId}/related_merge_requests`,
        {
            headers: {
                "PRIVATE-TOKEN": GITLAB_API_TOKEN
            }
        });
    const data = await res.json();
    return data;
    // console.log("getProjectIssueMRs", projectId, issueId, data);
}

export const updateIssueLabels = async (projectId, issueId, labels) => {
    const res = await fetch(`${GITLAB_API_URL}/projects/${projectId}/issues/${issueId}?labels=${labels.join(",")}`,
        {
            method: "PUT",
            headers: {
                "PRIVATE-TOKEN": GITLAB_API_TOKEN
            }
        }
    );

    return await res.json();
};
