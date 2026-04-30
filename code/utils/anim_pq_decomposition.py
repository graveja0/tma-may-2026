#!/usr/bin/env python3
"""
anim_pq_decomposition.py

Two-section equation animation for the TMA 2026 talk.

Section 1 (load):     Spending = P × Q
Section 2 (click 1):  P distributes into P^{Medicare} × M, leaving
                      Spending = P^{Medicare} × M × Q

Render:
  manim -qh --save_sections code/utils/anim_pq_decomposition.py PQDecomposition

Output: media/videos/anim_pq_decomposition/1080p60/PQDecomposition.mp4
"""

from manim import *

# Vanderbilt brand palette
COL_INK = "#1C1C1C"
COL_GOLD = "#CFAE70"
COL_OAK = "#946E24"
COL_CREAM = "#F5F3EF"


class PQDecomposition(Scene):
    """Two sections (load + 1 click) showing the decomposition
    of payment × quantity into Medicare price × multiplier × quantity."""

    def construct(self):
        self.camera.background_color = WHITE  # match slide background

        # ----- Section 1: simple P × Q --------------------------------
        # Split into parts so TransformMatchingTex can keep "× Q"
        # anchored on the right side of the screen.
        eq1 = MathTex(
            r"P",
            r"\times Q",
            color=COL_INK,
        ).scale(3.0)

        self.next_section("01_simple")
        self.play(Write(eq1), run_time=1.0)
        self.wait(1.0)

        # ----- Section 2: P distributes into P^{Medicare} × M ----------
        # M is highlighted in oak gold to draw attention to the multiplier
        # — the bilaterally-negotiated piece that has no system-wide brake.
        eq2 = MathTex(
            r"P^{\text{Medicare}}",
            r"\times",
            r"M",
            r"\times Q",
            color=COL_INK,
        ).scale(3.0)
        eq2[2].set_color(COL_OAK)  # M

        self.next_section("02_decomposed")
        self.play(TransformMatchingTex(eq1, eq2), run_time=1.5)
        self.wait(1.5)
