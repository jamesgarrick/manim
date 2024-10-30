from manim import *

class NielsenModel(Scene):
    def construct(self):
        equation = MathTex(
            "P_c = P_m \\times \\frac{1 - \\phi_f}{1 + \\frac{\\phi_f}{(L_f / 2W_f)}}"
        )
        self.play(Write(equation))
        self.wait(2)
