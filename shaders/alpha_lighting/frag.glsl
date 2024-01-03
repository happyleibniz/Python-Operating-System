#version 330

out vec4 fragColor;

uniform sampler2DArray u_TextureArraySampler;

in vec3 v_Position;
in vec3 v_TexCoords;
in float v_Light;


void main(void) {
	vec4 textureColor = texture(u_TextureArraySampler, v_TexCoords);

	if (textureColor.a <= 0.5) { // discard if texel's alpha component is 0 (texel is transparent)
		discard;
	}
    
	fragColor = textureColor * vec4(v_Light, v_Light, v_Light, 1.0);
}