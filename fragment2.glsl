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

vec3 hash31(float p) {
    vec3 p3 = fract(vec3(p) * vec3(0.1031, 0.1030, 0.0973));
    p3 += dot(p3, p3.yzx + 33.33);
    return fract((p3.xxy + p3.yzz) * p3.zyx);
}

void main() {
    float zoom = sin(uTime * 0.2) * 0.2 + 0.3;
    vec2 uv = gl_FragCoord.xy * zoom + 50.0 * uTime;
    vec3 color = vec3(0);

    int num = int(uv.x) & int(uv.y); // change the bitwise operator. It can be: (&, |, ^)
    if (isPrime(num)) color += hash31(num);
    
    fragColor = vec4(color, 1.0);
}