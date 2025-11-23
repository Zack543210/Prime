import pygame as pg
import moderngl as mgl
import numpy as np
import sys

class App:
    def __init__(self, winSize=(1920, 1080)):
        pg.init()
        self.WIN_SIZE = winSize

        #opengl settings
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)

        #opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        self.ctx = mgl.create_context()

        #mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)

        #time objects
        self.clock = pg.time.Clock()
        self.time = 0

        #load shaders
        with open('Projects/myProjects17 - Numbers/vertex.glsl') as f:
            vertex = f.read()
        with open('Projects/myProjects17 - Numbers/fragment.glsl') as f: # Change fragment to fragment2 if you want to change the picture
            # Also look at fragment.glsl.
            fragment = f.read()
        self.program = self.ctx.program(vertex_shader=vertex, fragment_shader=fragment)

        #quad screen vbo
        verticles = [(-1, -1, 0), (1, -1, 0), (1, 1, 0), (-1, 1, 0), (-1, -1, 0), (1, 1, 0)]
        vertexData = np.array(verticles, dtype='f4')
        self.vbo = self.ctx.buffer(vertexData)

        #quad vao
        self.vao = self.ctx.vertex_array(self.program, [(self.vbo, '3f', 'inPosition')]) #Change to cameltype if dosent work

        #shader uniforms
        self.setUniform('uResolution', self.WIN_SIZE) #Change to cameltype if dosent work

    def setUniform(self, uName, uValue):
        try:
            self.program[uName] = uValue
        except KeyError:
            pass

    def destroy(self):
        self.vbo.release()
        self.program.release()
        self.vao.release()

    def checkEvents(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.destroy()
                pg.quit()
                sys.exit()

    def getTime(self):
        self.time = pg.time.get_ticks() * 0.001

    def update(self):
        self.setUniform('uTime', self.time)
        self.setUniform('uMouse', pg.mouse.get_pos())
    
    def render(self):
        self.ctx.clear()
        self.vao.render()
        pg.display.flip()

    def run(self):
        while True:
            self.getTime()
            self.checkEvents()
            self.update()
            self.render()
            self.clock.tick(0)
            fps = self.clock.get_fps()
            pg.display.set_caption(f'{fps :.1f}')

if __name__ == '__main__':
    App().run()