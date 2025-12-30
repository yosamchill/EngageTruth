function formatNumber(num) {
    if (num >= 1_000_000) return (num / 1_000_000).toFixed(1) + "M"
    if (num >= 1_000) return (num / 1_000).toFixed(1) + "K"
    return num
}

async function analyze() {
    const username = document.getElementById("username").value.trim()
    if (!username) return

    const result = document.getElementById("result")
    const loading = document.getElementById("loading")
    const error = document.getElementById("error")
    const verdictBadge = document.getElementById("verdict-badge")

    error.classList.add("hidden")
    result.classList.add("hidden")
    result.classList.remove("show")
    loading.classList.remove("hidden")

    try {
        const res = await fetch(`http://127.0.0.1:8000/analyze/${username}`)
        if (!res.ok) throw new Error()

        const data = await res.json()

        loading.classList.add("hidden")
        result.classList.remove("hidden")

        document.getElementById("followers").innerText = formatNumber(data.followers)
        document.getElementById("engagement").innerText = data.engagement + "%"
        document.getElementById("score").innerText = data.risk_score
        document.getElementById("verdict").innerText = data.verdict

        verdictBadge.className = "verdict-pill"
        if (data.risk_score <= 30) verdictBadge.classList.add("low")
        else if (data.risk_score <= 60) verdictBadge.classList.add("medium")
        else verdictBadge.classList.add("high")

        setTimeout(() => result.classList.add("show"), 10)

    } catch {
        loading.classList.add("hidden")
        error.classList.remove("hidden")
        error.innerText = "could not analyze profile"
    }
}
