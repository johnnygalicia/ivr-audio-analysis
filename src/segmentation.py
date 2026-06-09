def merge_segments(segments, sr, min_silence):
    if len(segments) == 0:
        return []
    
    merged = []
    current_start = segments[0][0]
    current_end = segments[0][1]

    for start, end in segments[1:]:
        gap = (start - current_end) / sr
        
        if gap < min_silence:
            current_end = end
        else:
            merged.append((current_start, current_end))
            current_start = start
            current_end = end

    merged.append((current_start, current_end))
    return merged