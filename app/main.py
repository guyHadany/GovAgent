from app.agent import GovAgent


def main():
    print()
    print("🟢 GovAgent")
    print("-------------------------")

    agent = GovAgent()
    agent.start()

    opened = agent.open_procedure(
        "Solicitud de Licencia o Autorización Urbanística"
    )

    print(f"הליך נפתח: {opened}")

    if opened:
        downloaded_file = agent.download_form(
            "Descargar instancia",
            "output/solicitud_licencia_urbanistica.pdf"
        )

        print(f"קובץ הורד אל: {downloaded_file}")

    agent.wait()


if __name__ == "__main__":
    main()