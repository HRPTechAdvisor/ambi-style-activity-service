# test_endpoints.ps1
# Script to test FastAPI endpoints locally

$baseUrl = "http://127.0.0.1:8001"

$endpoints = @("/health", "/ready", "/metrics")

foreach ($ep in $endpoints) {
    Write-Host "Testing $ep ..."
    try {
        $response = Invoke-WebRequest -Uri "$baseUrl$ep" -UseBasicParsing
        Write-Host "Status Code: $($response.StatusCode)"
        Write-Host "Response Body:`n$($response.Content)`n"
    } catch {
        Write-Host ("Error accessing " + $ep + ": " + $_)
    }
}
