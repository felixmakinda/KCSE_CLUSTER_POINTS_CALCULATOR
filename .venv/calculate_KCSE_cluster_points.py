
# KCSE Grade Points Conversion Dictionary
GRADE_POINTS = {
    'A': 12,
    'A-': 11,
    'B+': 10,
    'B': 9,
    'B-': 8,
    'C+': 7,
    'C': 6,
    'C-': 5,
    'D+': 4,
    'D': 3,
    'D-': 2,
    'E': 1
}

def input_grades ():
    print ("\n--- Enter Subject Grades ---")
    subjects = {}
    while True:
        subject = input ("Enter subject name (or press Enter to finish): ").strip().upper()
        if not subject:
            break
        grade = input (f"Enter grade for {subject} (e.g., A, B-, C+): ").strip().upper()
        if grade not in GRADE_POINTS:
            print("Invalid grade. Please enter a valid grade like A, B+, C-, etc.")
            continue
        subjects[subject] = grade
    return subjects

def select_cluster_subjects (subjects):
    print ("\n --- Select 4 Cluster Subjects ---")
    print ("Available subjects:", ", ".join(subjects.keys()))
    cluster_subjects = []
    while len(cluster_subjects) < 4:
        subject = input(f"Select cluster subject {len(cluster_subjects)+1}: ").strip().upper()
        if subject not in subjects:
            print("Subject not found in entered list. Try again!")
            continue
        if subject in cluster_subjects:
            print("You have already selected this subject. Choose a different one.")
            continue
        cluster_subjects.append(subject)
    return cluster_subjects

def calculate_cluster_points (subjects, cluster_subjects, agp):
    max_agp = 84
    performance_index = agp / max_agp
    raw_cluster_points = sum(GRADE_POINTS[subjects[subj]] for subj in cluster_subjects)
    estimated_cluster_points = (raw_cluster_points / 48) * 48 * performance_index
    return raw_cluster_points, round (performance_index, 3), round(estimated_cluster_points, 2)

def main():
    print(" ==== KCSE Cluster Points Calculator ====")
    subjects = input_grades()
    if len(subjects) < 4:
        print("You must enter at least 4 subjects.")
        return

    try:
        agp = float (input("\nEnter total AGP (mean grade points out of 84: "))
        if agp <= 0 or agp > 84:
            raise ValueError
    except ValueError:
        print("Invalid AGP. Enter a number between 1 and 84.")
        return

    cluster_subjects = select_cluster_subjects(subjects)
    raw, perf_index, cluster = calculate_cluster_points(subjects, cluster_subjects, agp)

    print ("\n--------- Results -----------")
    print ("Selected Cluster Subjects:", ", ".join(cluster_subjects))
    print ("Raw Cluster Points (max 48):", raw)
    print ("Performance Index: ", perf_index)
    print ("Estimated Cluster Points:", cluster)

if __name__ == "__main__":
    main()

