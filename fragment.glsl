#version 330 core

layout(location = 0) out vec4 fragColor;

uniform vec2 uResolution;
uniform vec2 uMouse;
uniform float uTime;

bool isPrime(int n) {
    if (n == 2) return true;
    if (n < 2 || n % 2 == 0) return false;
    for (int i = 3; i <= int(sqrt(float(n))); i += 2) {
        if (n % i == 0) return false;
    }
    return true;
}

void main() {
    float zoom = uMouse.x / uResolution.x;
    vec2 uv = (floor(gl_FragCoord.xy) - floor(uResolution.xy * 0.5)) * zoom;
    vec3 color = vec3(0);

    uv.y += floor(uResolution.y * 0.5);
    int num = int(uv.y) * int(uResolution.x) + int(uv.x);
    if (isPrime(num)) color.g += 1.0;

    fragColor = vec4(color, 1.0);
}