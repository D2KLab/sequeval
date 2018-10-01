$(function () {
    $('#run-evaluator').submit(function () {
        $('.btn').prop('disabled', true);
        $('#result').empty();

        $.getJSON('/run', $(this).serialize(), function (json) {
            let profiler = json['profiler'];
            let result = $('#result');
            let h3 = $('<h3>').text('Profiler');
            result.append(h3);
            let ul = $('<ul>');
            result.append(ul);
            ul.append($('<li>').text('Users: ' + profiler['users']));
            ul.append($('<li>').text('Items: ' + profiler['items']));
            ul.append($('<li>').text('Ratings: ' + profiler['ratings']));
            ul.append($('<li>').text('Sequences: ' + profiler['sequences']));
            ul.append($('<li>').text('Sparsity: ' + profiler['sparsity']));
            ul.append($('<li>').text('Length: ' + profiler['length']));

            let splitter = json['splitter'];
            h3 = $('<h3>').text('Splitter');
            result.append(h3);
            ul = $('<ul>');
            result.append(ul);
            ul.append($('<li>').text('Training set: ' + splitter['training']));
            ul.append($('<li>').text('Test set: ' + splitter['test']));

            let evaluator = json['evaluator'];
            h3 = $('<h3>').text('Evaluator');
            result.append(h3);
            let table = $('<table>').addClass('table');
            result.append(table);
            let tr = $('<tr>');
            table.append(tr);
            tr.append($('<th>').text('Algorithm'));
            tr.append($('<th>').text('Coverage'));
            tr.append($('<th>').text('Precision'));
            tr.append($('<th>').text('nDPM'));
            tr.append($('<th>').text('Diversity'));
            tr.append($('<th>').text('Novelty'));
            tr.append($('<th>').text('Serendipity'));
            tr.append($('<th>').text('Confidence'));
            tr.append($('<th>').text('Perplexity'));
            for (let i = 0; i < evaluator.length; i++) {
                let tr = $('<tr>');
                table.append(tr);
                tr.append($('<td>').text(evaluator[i][0]));
                for (let j = 1; j < evaluator[i].length; j++) {
                    tr.append($('<td>').text(evaluator[i][j]));
                }
            }

            $('.btn').prop('disabled', false);
        });
        return false;
    });
});