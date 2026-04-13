
def add_recepients(to: list[str], cc: list[str] = []) -> None:
    
    if not isinstance(to, list):
        raise ValueError("Please make sure to return a list")
    
    if len(to) <= 0:
        raise ValueError("No receipients please make sure to put some reciepients")

    all_email = cc + to
    return all_email

