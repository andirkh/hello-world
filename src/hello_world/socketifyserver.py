from socketify import App

def run_socketify() -> None:
  app = App()
  app.get("/", lambda res, req: res.end("Hello World from Socketify!"))
  app.listen(8000, lambda config: print("Listening on port http://localhost:%d now\n" % config.port))
  app.run()