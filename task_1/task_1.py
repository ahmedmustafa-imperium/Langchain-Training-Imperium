from utils.env_loader import load_env
import os
def main():
    load_env()
    print ("Enviornment Variables loaded successfully")
    keys = [
            "AZURE_OPENAI_API_KEY",
            "AZURE_OPENAI_ENDPOINT",
            "DEPLOYMENT_NAME",
            "OPENAI_API_VERSION"
        ]
    missing = [var for var in keys if not os.getenv(var)]

    if missing:
        raise ValueError(f"❌ Missing environment variables: {', '.join(missing)}")
    else:
        print("All required environment variables are set.\n")

        # Print each variable (masked)
        for var in keys:
            value = os.getenv(var)
            masked_value = value[:4] + "****" if value else "****"
            print(f"{var}: {masked_value}")

if __name__ == "__main__":
    main()