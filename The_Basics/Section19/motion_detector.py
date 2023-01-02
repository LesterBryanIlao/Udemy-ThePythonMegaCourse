import cv2
import pandas as pd
from datetime import datetime

first_frame = None
status_list = [None, None]
times_list = []

df = pd.DataFrame(columns=["Start", "End"])

video = cv2.VideoCapture(1)

while True:
    check, frame = video.read()

    status = 0  # no motion

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)
    thresh_frame = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]
    thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

    (cnts, _) = cv2.findContours(thresh_frame.copy(),
                                 cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in cnts:
        if cv2.contourArea(cnt) < 1000:
            continue

        status = 1  # with motion

        (x, y, w, h) = cv2.boundingRect(cnt)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    status_list.append(status)

    status_list = status_list[-2:]
    
    status_cond1 = status_list[-1] == 0 and status_list[-2] == 1
    status_cond2 = status_list[-1] == 1 and status_list[-2] == 0

    if status_cond1:
        times_list.append(datetime.now())

    if status_cond2:
        times_list.append(datetime.now())

    # if status_list[-2] != status_list[-1]:
    #     times_list.append(datetime.now())

    cv2.imshow("Gray Frame", gray)
    cv2.imshow("Delta Frame", delta_frame)
    cv2.imshow("Threshold Frame", thresh_frame)
    cv2.imshow("Color Frame", frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        if status == 1:
            times_list.append(datetime.now())
        break

    print(f"Status: {status}")

print(status_list)
print(times_list)

for i in range(0, len(times_list), 2):
    # append version
    df = df.append(
        {"Start": times_list[i], "End": times_list[i+1]}, ignore_index=True)
    # df = pd.concat(
    #     df, pd.DataFrame([[times_list[i], times_list[i+1]]],
    #                  columns=["Start", "End"]))
    # pd.DataFrame({"Start": [times_list[i]], "End": [times_list[i+1]]}))

# df["Start"] = pd.to_datetime(df["Start"]).dt.date
# df["End"] = pd.to_datetime(df["End"]).dt.date

fmt = '%H:%M'  # or: infer_datetime_format=True

# df['SOM'] = pd.to_datetime(df['Start'],
#                            format=fmt,
#                            errors='coerce')
# df['EOM'] = pd.to_datetime(df['End'],
#                            format=fmt,
#                            errors='coerce')

# df['Duration of Motion'] = df.EOM - df.SOM


df["Duration"] = df.End - df.Start

df.to_csv("CSV-files/MotionRecords.csv")

video.release()
cv2.destroyAllWindows()
