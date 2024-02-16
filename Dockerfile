FROM nixos/nix

WORKDIR /app

COPY . .

RUN nix-shell --run "pdm install"

EXPOSE 8000

CMD ["nix-shell", "--run", "pdm run start"]