from manim import *


class Intro(Scene):
    def construct(self):
        li = TextMobject("Line Integral", color=BLUE)
        li.scale(2)

        int2 = TexMobject(r"\int_C\overrightarrow{\textbf{F}} \bullet \textbf{d} \overrightarrow{\textbf{r}}")
        int2.scale(1.5)

        int1 = TexMobject(r"\int_C f(x,y) ds")
        int1.scale(1.5)

        int3 = TexMobject(r"\int_C \textbf{P}dx + \textbf{Q}dy")
        int3.scale(1.5)

        uses = BulletedList(
            "Work",
            "Center of mass",
            "Faraday's Law",
            "Ampere's Law",
            "..."
        )

        self.play(Write(li))
        self.wait()
        self.play(ApplyMethod(li.shift, 3 * UP))

        self.play(Write(int1))
        self.wait()

        self.play(Transform(int1, int2))
        self.wait()

        self.play(Transform(int1, int3))
        self.wait()

        self.play(Uncreate(int1))
        self.play(Write(uses))

        self.wait(2)


class ScalarField(ThreeDScene):
    def construct(self):
        t_config = {
            "x_min": -1,
            "x_max": 1,
            "y_min": -1,
            "y_max": 1,
            "z_axis_config": {},
            "z_min": -1,
            "z_max": 1,
            "z_normal": DOWN,
            "num_axis_pieces": 20,
            "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
            "number_line_config": {
                "include_tip": False,
            },
        }

        title = TextMobject("Scalar Fields", color=ORANGE)
        title.scale(2)

        axes = ThreeDAxes(
            **t_config
        )

        func = ParametricSurface(
            self.func,
            resulution=(16, 24),
            u_min=-1,
            u_max=1,
            v_min=-1,
            v_max=1,
            fill_color=YELLOW,
            checkerboard_colors=[YELLOW, ORANGE]
        )

        func.scale(2)
        axes.scale(2)

        self.play(Write(title))
        self.wait()

        self.play(Uncreate(title))
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)

        self.play(ShowCreation(axes), ShowCreation(func))
        self.begin_ambient_camera_rotation()
        self.wait(30)

    @staticmethod
    def func(u, v):
        return np.array([
            u,
            v,
            u ** 2 + v ** 2,
        ])


class Equation(Scene):
    def construct(self):
        eq = TexMobject("f(x,y) = x^2+y^2")
        eq.scale(2)
        self.play(Write(eq))
        self.wait()


class ArcLength(Scene):
    def construct(self):
        g_config = {
            "propagate_style_to_family": True,
            "three_d": False,
            "number_line_config": {
                "color": LIGHT_GREY,
                "include_tip": True,
            },
            "x_axis_config": {},
            "y_axis_config": {
                "label_direction": LEFT,
            },
            "x_min": 0,
            "x_max": 2,
            "y_min": 0,
            "y_max": 2,
            "default_num_graph_points": 100,
        }

        curve = ParametricFunction(
            self.func,
            t_min=0,
            t_max=2,
            color=BLUE
        )

        axes = Axes(
            **g_config
        )

        heading = TextMobject("Arc Length", color=YELLOW)
        heading.scale(2)

        text = TexMobject(r"\langle x(t), y(t) \rangle")
        text.shift(2.5 * RIGHT + 2 * UP)
        text.scale(0.5)

        func = VGroup(axes, curve, text)
        func.scale(2)
        func.move_to(ORIGIN)

        t1 = Line(0.5 * LEFT + 1 * DOWN, 1 * DOWN + 1.25 * LEFT, color=GREEN)
        t2 = Line(0.5 * LEFT + 1 * DOWN, 0.5 * LEFT + 3.25 * UP, color=RED)

        t3 = Line(1 * DOWN + 1.25 * LEFT, 0.5 * LEFT + 3.25 * UP, color=YELLOW)

        b1 = Brace(VGroup(t1), DOWN, color=GREEN)
        dx = b1.get_tex(r"\Delta x")

        b2 = Brace(VGroup(t2), RIGHT, color=RED)
        dy = b2.get_tex(r"\Delta y")

        b3 = Brace(
            VGroup(t3),
            np.array([
                -0.99388, 0.16, 0
            ]))
        d = b3.get_tex(r"\Delta s")

        self.play(Write(heading))
        self.wait()

        self.play(ApplyMethod(heading.shift, 3.5 * UP))

        self.play(ShowCreation(func))
        self.wait()

        self.play(ApplyMethod(func.scale, 4), Uncreate(heading))
        self.wait()

        self.play(ShowCreation(t1), ShowCreation(t2))
        self.wait()

        self.play(ShowCreation(b1), ShowCreation(dx))
        self.wait()

        self.play(ShowCreation(b2), ShowCreation(dy))
        self.wait()

        self.play(ShowCreation(t3), ShowCreation(b3), ShowCreation(d))
        self.wait()

    @staticmethod
    def func(t):
        return np.array([
            t,
            np.sin(5 * t) * t + 1,
            0
        ])


class ArcExp(Scene):
    def construct(self):
        step1 = TexMobject(r"\Delta s = \sqrt{{\Delta x}^2 + "
                           r"{\Delta y}^2}}"
                           )
        step1.scale(1.5)

        step2 = TexMobject(r"\sum_{i=1}^{n}{\sqrt{{\Delta x_i}^2 + "
                           r"{\Delta y_i}^2}}}"
                           )
        step2.scale(1.5)

        step3 = TexMobject(r"\lim_{n \rightarrow \infty} "
                           r"\sum_{i=1}^{n}{\sqrt{{\Delta x_i}^2 + {\Delta y_i}^2}}}"
                           )
        step3.scale(1.5)

        step4 = TexMobject(
            r"\lim_{n \rightarrow \infty} \sum_{i=1}^{n}{\sqrt{(\frac{\Delta x_i}{\Delta t})^2 +"
            r"(\frac{\Delta y_i}{\Delta t})^2} \Delta t}}"
        )
        step4.scale(1.5)

        step5 = TexMobject(
            r"\int_a^b {\sqrt{(\frac{dx}{dt})^2 +"
            r"(\frac{dy}{dt})^2}dt}}"
        )
        step5.scale(1.5)

        step6 = TexMobject(
            r"\int_a^b ds"
        )
        step6.scale(1.5)
        step6.shift(2 * DOWN)

        equal = TexMobject(r"=")
        equal.scale(1.5)

        self.play(Write(step1))
        self.wait()

        self.play(Transform(step1, step2))
        self.wait()

        self.play(Transform(step1, step3))
        self.wait()

        self.play(Transform(step1, step4))
        self.wait()

        self.play(Transform(step1, step5))
        self.wait()

        self.play(
            ApplyMethod(step1.shift, 2 * UP),
            Write(step6),
            Write(equal)
        )

        self.wait()


class LineIntegralScalar(ThreeDScene):

    def construct(self):
        t_config = {
            "x_min": -1,
            "x_max": 1,
            "y_min": -1,
            "y_max": 1,
            "z_axis_config": {},
            "z_min": -1,
            "z_max": 1,
            "z_normal": DOWN,
            "num_axis_pieces": 20,
            "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
            "number_line_config": {
                "include_tip": False,
            },
        }

        integral = TexMobject(r"\int_C f(x,y) ds")
        integral.scale(2)
        integral2 = TexMobject(r"\int_C f(x,y) ds")
        integral2.scale(2)

        sol = TexMobject(r"\int_a^b f(x(t), y(t)) \sqrt{(\frac{dx}{dt})^2+(\frac{dy}{dt})^2}dt")
        sol.scale(1.5)

        surface = ParametricSurface(
            self.func,
            resulution=(16, 24),
            u_min=-1,
            u_max=1,
            v_min=-1,
            v_max=1,
            fill_color=RED,
            checkerboard_colors=[RED, ORANGE]

        )

        curve = ParametricFunction(
            self.c,
            t_min=-1,
            t_max=1,
        )

        curve_p = ParametricFunction(
            self.c_project,
            t_min=-1,
            t_max=1
        )

        surface.scale(2)
        axes = ThreeDAxes(**t_config)
        axes.scale(2.5)

        point1 = Point(self.c(-1))
        point2 = Point(self.c(1))

        text = TextMobject("C")
        text.scale(1.5)
        text.move_to(curve, 4 * RIGHT + 3 * DOWN)

        area = self.get_riemann_sums(self.c_project, dx=0.005)

        self.play(Write(integral))

        self.play(ApplyMethod(integral.scale, 0.5))
        self.play(ApplyMethod(integral.shift, 3 * UP))

        self.play(ShowCreation(axes))
        self.play(ShowCreation(surface))
        self.play(ShowCreation(curve), Write(text))
        self.play(Uncreate(integral), Uncreate(text))
        self.move_camera(0.8 * np.pi / 2, -0.45 * np.pi)

        self.begin_ambient_camera_rotation()
        self.wait(6)

        self.stop_ambient_camera_rotation()
        self.move_camera(np.pi / 2, -np.pi / 2)
        self.play(Transform(curve, curve_p), Uncreate(surface))
        self.play(ShowCreation(area), ShowCreation(curve_p))

        self.wait(3)

        self.move_camera(0, -np.pi / 2)
        self.play(Uncreate(axes), Uncreate(curve), Uncreate(area), Uncreate(curve_p))

        self.play(Write(integral2))

        self.wait()

        self.play(Transform(integral2, sol))
        self.wait(6)

    @staticmethod
    def func(x, y):
        return np.array([
            x,
            y,
            0.5 * (math.cos(5 * x) + math.sin(5 * y))
        ])

    def c(self, t):
        return np.array([
            t,
            t ** 3,
            self.func(t, t ** 3)[-1]
        ])

    def c_project(self, t):
        return np.array([
            t,
            0,
            self.func(t, t ** 3)[-1]
        ])

    @staticmethod
    def get_riemann_sums(func, dx=0.2, x=(-1, 1), color=RED):
        rects = VGroup()
        for i in np.arange(x[0], x[1], dx):
            h = func(i)[-1]
            rect = Rectangle(height=h, width=dx, color=color)
            rect.shift(i * RIGHT + (h / 2) * OUT)
            rect.rotate(np.pi / 2, axis=X_AXIS)
            rect.rotate(-np.pi / 2, axis=Z_AXIS)
            rects.add(rect)

        return rects


class Example(Scene):
    def construct(self):
        axes_config = {"x_min": 0,
                       "x_max": 3,
                       "y_min": -1,
                       "y_max": 6,
                       "z_axis_config": {},
                       "z_min": -1,
                       "z_max": 1,
                       "z_normal": DOWN,
                       "num_axis_pieces": 20,
                       "light_source": 9 * DOWN + 7 * LEFT + 10 * OUT,
                       "number_line_config": {
                           "include_tip": False,
                       },
                       }

        axes = Axes(**axes_config)
        curve = ParametricFunction(
            self.func,
            t_min=0,
            t_max=1,
            color=RED
        )
        func = VGroup(axes, curve)
        func.move_to(ORIGIN + 3 * LEFT)
        func.scale(0.75)

        question = TextMobject(
            r"Evaluate $\int_C (3x^2 - 2y) ds$ \\where C is the line segment \\from $(3,6)$ to $(1,−1)$.")
        question.scale(1.5)

        step1 = TexMobject(r"C = \langle 3 - 2t, 6-7t \rangle \ 0 \leq t \leq 1")
        step1.move_to(2 * RIGHT + 1.5 * UP)
        step1.scale(0.75)

        step2 = TexMobject(r"\frac{dx}{dt} = -2, \frac{dy}{dt} = -7")
        step2.move_to(2 * RIGHT + 0.5 * UP)
        step2.scale(0.75)

        step3 = TexMobject(r"ds = \sqrt{(-2)^2 + (-7)^2} dt = \sqrt{53} \ dt")
        step3.move_to(2 * RIGHT + 0.5 * DOWN)
        step3.scale(0.75)

        step4 = TexMobject(r"\int_C (3x^2 - 2y) \ ds")
        step4.move_to(2 * RIGHT + 1.5 * DOWN)
        step4.scale(0.75)

        equal = TexMobject("=")
        equal.move_to(2 * RIGHT + 2 * DOWN)
        equal.scale(0.5)

        step5 = TexMobject(r"\int_0^1 (3(3 - 2t)^2 - 2(6 - 7t)^2) \sqrt{53} \ dt")
        step5.move_to(2 * RIGHT + 3 * DOWN)
        step5.scale(0.75)

        ans = TexMobject(r"8 \sqrt{53}")
        ans.move_to(2 * RIGHT + 3 * DOWN)

        self.play(Write(question))
        self.wait()

        self.play(ApplyMethod(question.scale, 0.5))
        self.play(ApplyMethod(question.shift, 3 * UP + 2 * RIGHT))
        self.wait()

        self.play(ShowCreation(func))
        self.wait()

        self.play(Write(step1))
        self.wait()

        self.play(Write(step2))
        self.wait()

        self.play(Write(step3))
        self.wait()

        self.play(Write(step4))
        self.play(Write(equal))
        self.wait()

        self.play(Write(step5))
        self.wait()

        self.play(Transform(step5, ans))
        self.wait()

    @staticmethod
    def func(t):
        return np.array([
            3 - 2 * t,
            6 - 7 * t,
            0
        ])


class VectorField(Scene):
    CONFIG = {
        "plane_kwargs": {
            "color": RED_B
        },
        "color_list": ['#e22b2b', '#e88e10', '#eae600', '#88ea00',
                       '#00eae2', '#0094ea', "#2700ea", '#bf00ea', '#ea0078'],
        "prop": 0
    }

    def construct(self):
        plane = NumberPlane(**self.plane_kwargs)
        plane.main_lines.fade(.9)
        plane.add(plane.get_axis_labels())
        self.add(plane)

        field = VGroup(*[self.calc_field(x * RIGHT + y * UP)
                         for x in np.arange(-9, 9, 1)
                         for y in np.arange(-5, 5, 1)
                         ])

        field_color = VGroup(*[self.calc_field_color(x * RIGHT + y * UP)
                         for x in np.arange(-9, 9, 1)
                         for y in np.arange(-5, 5, 1)
                         ])

        self.play(ShowCreation(field))
        self.wait(2)

    def calc_field_color(self, point):
        x, y = point[:2]
        func = np.array([x, y])
        magnitude = math.sqrt(func[0] ** 2 + func[1] ** 2)
        func = func / magnitude
        func = func / 1.5
        v = int(magnitude / 10 ** self.prop)
        index = len(self.color_list) - 1 if v > len(self.color_list) - 1 else v
        c = self.color_list[index]
        return Vector(func, color=c).shift(point)

    @staticmethod
    def calc_field(point):
        x, y = point[:2]
        func = np.array([x, y])
        return Vector(func).shift(point)
