async function analyze() {
    const username = document.getElementById("username").value
    if (!username) return

    document.getElementById("loading").classList.remove("hidden")
    document.getElementById("result").classList.add("hidden")

    const res = await fetch(`/analyze/${username}`)
    const data = await res.json()

    document.getElementById("followers").innerText = data.followers
    document.getElementById("engagement").innerText = data.engagement
    document.getElementById("score").innerText = data.risk_score
    document.getElementById("verdict").innerText = data.verdict

    document.getElementById("loading").classList.add("hidden")
    document.getElementById("result").classList.remove("hidden")
}
